import unittest

from transip.service import DomainService
from transip.client import MODE_RO, MODE_RW
from transip.service.objects import DnsEntry

try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import patch, Mock


class TestDomainService(unittest.TestCase):

    @patch('transip.client.SudsClient')
    def setUp(self, mock_client):
        super(TestDomainService, self).setUp()
        self.service = DomainService(login='sundayafternoon')
        self.service.build_cookie = Mock(return_value={"cookie": "value"})
        self.service.update_cookie = Mock()

        self.i = mock_client.return_value

    def set_return_value(self, method, value):
        getattr(self.i.service, method).return_value = value

    def _generic_test(self, soap_method, method, result, parameters=(), mode=MODE_RO):
        self.set_return_value(soap_method, result)
        # CALL
        soap_result = getattr(self.service, method)(*parameters)

        # VERIFY
        self.service.build_cookie.assert_called_with(mode=mode, method=soap_method, parameters=parameters)
        self.service.update_cookie.assert_called_with({"cookie": "value"})

        getattr(self.i.service, soap_method).assert_called_with(*parameters)
        self.assertEqual(soap_result, result)

    def test_constructor(self):
        # CALL
        ds = DomainService(login='sundayafternoon')
        # VERIFY
        self.assertEqual(ds.url, 'https://api.transip.nl/wsdl/?service=DomainService')

    @patch('transip.client.SudsClient')
    def test_get_domains(self, mock_client):
        # SETUP
        ds = DomainService('sundayafternoon')
        ds.build_cookie = Mock(return_value={"cookie": "value"})
        ds.update_cookie = Mock()

        i = mock_client.return_value
        i.service.getDomainNames.return_value = ['domain1', 'domain2']

        # CALL
        result = ds.get_domain_names()

        # VERIFY
        ds.build_cookie.assert_called_with(mode=MODE_RO, method='getDomainNames', parameters=())
        ds.update_cookie.assert_called_with({"cookie": "value"})
        i.service.getDomainNames.assert_called_with()
        self.assertEqual(result, ['domain1', 'domain2'])

    @patch('transip.client.SudsClient')
    def test_get_info(self, mock_client):
        # SETUP
        ds = DomainService(login='sundayafternoon')
        ds.build_cookie = Mock(return_value={"cookie": "value"})
        ds.update_cookie = Mock()

        i = mock_client.return_value
        getinfo_result = Mock()
        getinfo_result.dnsEntries = [DnsEntry('testentry', 86400, DnsEntry.TYPE_A, '127.0.0.1')]
        i.service.getInfo.return_value = getinfo_result

        # CALL
        result = ds.get_info('example.com')

        # VERIFY
        ds.build_cookie.assert_called_with(mode=MODE_RO, method='getInfo', parameters=['example.com'])
        ds.update_cookie.assert_called_with({"cookie": "value"})
        i.service.getInfo.assert_called_with('example.com')
        self.assertEqual(result, getinfo_result)

    @patch('transip.client.SudsClient')
    def test_set_dns_entries(self, mock_client):
        # SETUP
        ds = DomainService('sundayafternoon')
        ds.build_cookie = Mock(return_value={"cookie": "value"})
        ds.update_cookie = Mock()

        i = mock_client.return_value
        i.service.setDnsEntries.return_value = None

        dns_entry = DnsEntry('testentry', 86400, DnsEntry.TYPE_A, '127.0.0.1')

        # CALL
        result = ds.set_dns_entries('domain1', [dns_entry, ])

        # VERIFY
        ds.build_cookie.assert_called_with(mode=MODE_RW, method='setDnsEntries', parameters=('domain1', [dns_entry, ]))
        ds.update_cookie.assert_called_with({"cookie": "value"})
        i.service.setDnsEntries.assert_called_with('domain1', [dns_entry, ])

    @patch('transip.client.SudsClient')
    def test_add_dns_entries(self, mock_client):
        ds = DomainService('sundayafternoon')
        ds.build_cookie = Mock(return_value={'cookie': 'value'})
        ds.update_cookie = Mock()
        getinfo_result = Mock()
        dns_entry1 = DnsEntry(
            'testentry1',
            86400,
            DnsEntry.TYPE_A,
            '127.0.0.1',
        )
        dns_entry2 = DnsEntry(
            'testentry2',
            86400,
            DnsEntry.TYPE_A,
            '127.0.0.1',
        )
        getinfo_result.dnsEntries = [
            dns_entry1,
            dns_entry2,
        ]
        mock_client.return_value.service.getInfo.return_value = getinfo_result
        dns_entry3 = DnsEntry(
            'testentry3',
            86400,
            DnsEntry.TYPE_A,
            '127.0.0.1',
        )
        ds.add_dns_entries('domain1', [dns_entry3])
        mock_client.return_value.service.setDnsEntries.assert_called_with(
            'domain1',
            [dns_entry1, dns_entry2, dns_entry3],
        )

    @patch('transip.client.SudsClient')
    def test_remove_dns_entries(self, mock_client):
        ds = DomainService('sundayafternoon')
        ds.build_cookie = Mock(return_value={'cookie': 'value'})
        ds.update_cookie = Mock()
        getinfo_result = Mock()
        dns_entry1 = DnsEntry(
            'testentry1',
            86400,
            DnsEntry.TYPE_A,
            '127.0.0.1',
        )
        dns_entry2 = DnsEntry(
            'testentry2',
            86400,
            DnsEntry.TYPE_A,
            '127.0.0.1',
        )
        getinfo_result.dnsEntries = [
            dns_entry1,
            dns_entry2,
        ]
        mock_client.return_value.service.getInfo.return_value = getinfo_result
        ds.remove_dns_entries('domain1', [dns_entry1])
        mock_client.return_value.service.setDnsEntries.assert_called_with(
            'domain1',
            [dns_entry2],
        )

    def test_batch_check_availability(self):
        self._generic_test(
            soap_method='batchCheckAvailability',
            method='batch_check_availability',
            result='mock',
            parameters=(['example.com', 'example.nl'],),
            mode=MODE_RO
        )

        with self.assertRaises(ValueError):
            self._generic_test(
                soap_method='batchCheckAvailability',
                method='batch_check_availability',
                result='mock',
                parameters=(['example.com', 'example.nl'] * 11,),
                mode=MODE_RO
            )

    def test_check_availability(self):
        self._generic_test(
            soap_method='checkAvailability',
            method='check_availability',
            result='mock',
            parameters=('example.com',),
            mode=MODE_RO
        )

    def test_get_whois(self):
        self._generic_test(
            soap_method='getWhois',
            method='get_whois',
            result='mock',
            parameters=('example.com',),
            mode=MODE_RO
        )

    def test_get_domain_names(self):
        self._generic_test(
            soap_method='getDomainNames',
            method='get_domain_names',
            result=['mock', 'mock2'],
            mode=MODE_RO
        )

    def test_batch_get_info(self):
        self._generic_test(
            soap_method='batchGetInfo',
            method='batch_get_info',
            result=['mock', 'mock2'],
            parameters=('example.com',),
            mode=MODE_RO
        )

    def test_get_auth_code(self):
        self._generic_test(
            soap_method='getAuthCode',
            method='get_auth_code',
            result='string',
            parameters=('example.com',),
            mode=MODE_RO
        )

    def test_get_is_locked(self):
        self._generic_test(
            soap_method='getIsLocked',
            method='get_is_locked',
            result=True,
            parameters=('example.com',),
            mode=MODE_RO
        )

    def test_register(self):
        self._generic_test(
            soap_method='register',
            method='register',
            result='string',
            parameters=('example.com',),
            mode=MODE_RW
        )

    def test_cancel(self):
        self._generic_test(
            soap_method='cancel',
            method='cancel',
            result='string',
            parameters=('example.com', 'domain'),
            mode=MODE_RW
        )

    def test_transfer_with_owner_change(self):
        self._generic_test(
            soap_method='transferWithOwnerChange',
            method='transfer_with_owner_change',
            result='string',
            parameters=('example.com', 'authcode'),
            mode=MODE_RW
        )

    def test_transfer_without_owner_change(self):
        self._generic_test(
            soap_method='transferWithoutOwnerChange',
            method='transfer_without_owner_change',
            result='string',
            parameters=('example.com', 'authcode'),
            mode=MODE_RW
        )

    def test_set_nameservers(self):
        self._generic_test(
            soap_method='setNameservers',
            method='set_nameservers',
            result='string',
            parameters=('example.com', 'nameservers'),
            mode=MODE_RW
        )

    def test_set_lock(self):
        self._generic_test(
            soap_method='setLock',
            method='set_lock',
            result='string',
            parameters=('example.com',),
            mode=MODE_RW
        )

    def test_unset_lock(self):
        self._generic_test(
            soap_method='unsetLock',
            method='unset_lock',
            result='string',
            parameters=('example.com',),
            mode=MODE_RW
        )

    def test_set_owner(self):
        self._generic_test(
            soap_method='setOwner',
            method='set_owner',
            result='string',
            parameters=('example.com', 'registrant_whois_contact'),
            mode=MODE_RW
        )

    def test_set_contacts(self):
        self._generic_test(
            soap_method='setContacts',
            method='set_contacts',
            result='string',
            parameters=('example.com', 'contacts'),
            mode=MODE_RW
        )

    def test_get_all_tld_infos(self):
        self._generic_test(
            soap_method='getAllTldInfos',
            method='get_all_tld_infos',
            result='string',
            mode=MODE_RO
        )

    def test_get_tld_info(self):
        self._generic_test(
            soap_method='getTldInfo',
            method='get_tld_info',
            result='string',
            parameters=('.com',),
            mode=MODE_RO
        )

    def test_get_current_domain_action(self):
        self._generic_test(
            soap_method='getCurrentDomainAction',
            method='get_current_domain_action',
            result='string',
            parameters=('example.com',),
            mode=MODE_RO
        )

    def test_retry_current_domain_action_with_new_data(self):
        self._generic_test(
            soap_method='retryCurrentDomainActionWithNewData',
            method='retry_current_domain_action_with_new_data',
            result='string',
            parameters=('example.com',),
            mode=MODE_RO
        )

    def test_retry_transfer_with_different_auth_code(self):
        self._generic_test(
            soap_method='retryTransferWithDifferentAuthCode',
            method='retry_transfer_with_different_auth_code',
            result='string',
            parameters=('example.com', 'new_auth_code'),
            mode=MODE_RO
        )

    def test_cancel_domain_action(self):
        self._generic_test(
            soap_method='cancelDomainAction',
            method='cancel_domain_action',
            result='string',
            parameters=('example.com',),
            mode=MODE_RO
        )

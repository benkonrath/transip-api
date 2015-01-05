import unittest
from mock import patch, Mock

from transip.service import DomainService
from transip.client import MODE_RO, MODE_RW
from transip.service.dns import DnsEntry

class TestDomainService(unittest.TestCase):
        
    def testConstructor(self):
        # CALL
        ds = DomainService()
        # VERIFY
        self.assertEqual(ds.url, 'https://api.transip.nl/wsdl/?service=DomainService')  

    @patch('suds.client.Client')
    def testGetDomains(self, mock_client):
        # SETUP
        ds = DomainService()
        ds.build_cookie = Mock(return_value={"cookie":"value"})
        ds.update_cookie = Mock()

        i = mock_client.return_value
        i.service.getDomainNames.return_value = [ 'domain1', 'domain2' ]


        # CALL
        result = ds.get_domain_names()
        

        # VERIFY
        ds.build_cookie.assert_called_with(mode=MODE_RO, method='getDomainNames')
        ds.update_cookie.assert_called_with({"cookie":"value"})
        i.service.getDomainNames.assert_called_with()
        self.assertEqual(result, [ 'domain1', 'domain2' ])

    @patch('suds.client.Client')
    def testGetInfo(self, mock_client):
        # SETUP
        ds = DomainService()
        ds.build_cookie = Mock(return_value={"cookie":"value"})
        ds.update_cookie = Mock()

        i = mock_client.return_value
        i.service.getInfo.return_value = [ 'foo' ]

        # CALL
        result = ds.get_info('example.com')

        # VERIFY
        ds.build_cookie.assert_called_with(mode=MODE_RO, method='getInfo', parameters=['example.com'])
        ds.update_cookie.assert_called_with({"cookie":"value"})
        i.service.getInfo.assert_called_with('example.com')
        self.assertEqual(result, [ 'foo' ])

    @patch('suds.client.Client')
    def testSetDnsEntries(self, mock_client):
        # SETUP
        ds = DomainService()
        ds.build_cookie = Mock(return_value={"cookie": "value"})
        ds.update_cookie = Mock()

        i = mock_client.return_value
        i.service.setDnsEntries.return_value = None

        dns_entry = DnsEntry('testentry', 86400, DnsEntry.TYPE_A, '127.0.0.1')

        # CALL
        result = ds.set_dns_entries('domain1', [dns_entry, ])

        # VERIFY
        ds.build_cookie.assert_called_with(mode=MODE_RW, method='setDnsEntries', parameters=['domain1', [dns_entry, ]])
        ds.update_cookie.assert_called_with({"cookie": "value"})
        i.service.setDnsEntries.assert_called_with('domain1', [dns_entry, ])

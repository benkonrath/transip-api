import unittest

from transip.client import MODE_RO, MODE_RW
from transip.service.objects import MailBox, MailForward, WebHost
from transip.service.webhosting import WebhostingService

try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import patch, Mock


class TestWebhostingService(unittest.TestCase):

    @patch('transip.client.SudsClient')
    def setUp(self, mock_client):
        self.service = WebhostingService(login='sundayafternoon')
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

    def testConstructor(self):
        vs = WebhostingService(login='sundayafternoon')
        self.assertEqual(vs.url, 'https://api.transip.nl/wsdl/?service=WebhostingService')

    def test_available_packages(self):
        self._generic_test(
            soap_method='getAvailablePackages',
            method='get_available_packages',
            result=['Webhosting s', 'Webhosting l', 'Webhosting xl', 'Email only']
        )

    def test_webhosting_domain_names(self):
        self._generic_test(
            soap_method='getWebhostingDomainNames',
            method='get_webhosting_domain_names',
            result=['example.com', 'since we are mocking, the results do not mater']
        )

    def test_info(self):
        self._generic_test(
            soap_method='getInfo',
            method='get_info',
            result=WebHost('example.com'),
            parameters=('example.com', )
        )

    def test_create_mailbox(self):
        mailbox = MailBox('info@example.com')
        self._generic_test(
            soap_method='createMailBox',
            method='create_mailbox',
            result=mailbox,
            parameters=('info@example.com', mailbox),
            mode=MODE_RW
        )

    def test_update_mailbox(self):
        self._generic_test(
            soap_method='modifyMailBox',
            method='update_mailbox',
            result='mock',
            parameters=('info@example.com', 'mock'),
            mode=MODE_RW
        )

    def test_delete_mailbox(self):
        self._generic_test(
            soap_method='deleteMailBox',
            method='delete_mailbox',
            result='mock',
            parameters=('info@example.com', 'mock'),
            mode=MODE_RW
        )
        
    def test_create_mail_forward(self):
        mail_forward = MailForward('test', 'info@example.com')
        self._generic_test(
            soap_method='createMailForward',
            method='create_mail_forward',
            result=mail_forward,
            parameters=('info@example.com', mail_forward),
            mode=MODE_RW
        )

    def test_update_mail_forward(self):
        self._generic_test(
            soap_method='modifyMailForward',
            method='update_mail_forward',
            result='mock',
            parameters=('info@example.com', 'mock'),
            mode=MODE_RW
        )

    def test_delete_mail_forward(self):
        self._generic_test(
            soap_method='deleteMailForward',
            method='delete_mail_forward',
            result='mock',
            parameters=('info@example.com', 'mock'),
            mode=MODE_RW
        )

    def test_get_available_upgrades(self):
        self._generic_test(
            soap_method='getAvailableUpgrades',
            method='get_available_upgrades',
            result='mock',
            parameters=('example.com',),
            mode=MODE_RO
        )

    def test_set_mailbox_password(self):
        self._generic_test(
            soap_method='setMailBoxPassword',
            method='set_mailbox_password',
            result='mock',
            parameters=('example.com', 'mailbox', 'password'),
            mode=MODE_RW
        )

import unittest

from transip.client import MODE_RO, MODE_RW
from transip.service import VpsService

try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import patch, Mock

class TestVPSService(unittest.TestCase):

    def testConstructor(self):
        # CALL
        vs = VpsService(login='sundayafternoon')
        # VERIFY
        self.assertEqual(vs.url, 'https://api.transip.nl/wsdl/?service=VpsService')

    @patch('transip.client.SudsClient')
    def testGetVpses(self, mock_client):
        # SETUP
        vs = VpsService(login='sundayafternoon')
        vs.build_cookie = Mock(return_value={"cookie":"value"})
        vs.update_cookie = Mock()

        i = mock_client.return_value
        i.service.getVpses.return_value = ['vps1', 'vps2']

        # CALL
        result = vs.get_vpses()

        # VERIFY
        vs.build_cookie.assert_called_with(mode=MODE_RO, method='getVpses')
        vs.update_cookie.assert_called_with({"cookie": "value"})
        i.service.getVpses.assert_called_with()
        self.assertEqual(result, [ 'vps1', 'vps2' ])

    @patch('transip.client.SudsClient')
    def testSetCustomerLock(self, mock_client):
        # SETUP
        vs = VpsService(login='sundayafternoon')
        vs.build_cookie = Mock(return_value={"cookie":"value"})
        vs.update_cookie = Mock()

        i = mock_client.return_value
        i.service.setCustomerLock.return_value = None

        # CALL
        result = vs.set_customer_lock(vps_name='test',enabled=1)

        # VERIFY
        vs.build_cookie.assert_called_with(mode=MODE_RW, method='setCustomerLock', parameters=['test',1])
        vs.update_cookie.assert_called_with({"cookie": "value"})
        i.service.setCustomerLock.assert_called_with('test', 1)
        self.assertEqual(result, None)

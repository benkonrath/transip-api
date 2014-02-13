import unittest
from mock import patch, Mock

import transip.client
from transip.service import DomainService
from transip.client import MODE_RO

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

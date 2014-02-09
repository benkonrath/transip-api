import unittest
import mock
from mock import patch

import transip.client
from transip.service import DomainService

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

        # CALL
        result = ds.get_domain_names()

        # VERIFY
        self.assertEqual(result, [])
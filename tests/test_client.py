# vim: set fileencoding=utf-8 :
import unittest
import mock
from mock import patch, Mock

import suds

import transip
from transip.client import Client, MODE_RO

class TestClient(unittest.TestCase):

    @patch('suds.client.Client')
    def testConstructor(self, mock_client):
        # CALL
        c = Client('TestService')

        # VERIFY
        self.assertEqual(c.service_name, 'TestService')
        self.assertEqual(c.url, 'https://api.transip.nl/wsdl/?service=TestService')

    @patch('suds.client.Client')
    def testSignatureIsCorrect(self, mock_client):
        # SETUP
        reference1 = 'ZurqqM1HQTWqYb5IOFYEk%2BGw7a2I%2FknIHEw9lJag%2FnHDp3XfZYj%2F89GTjM52x6spJEJtUnUpSZ02DsVoaJlGl4iZEMk0%2FbWcP5ODRJhASHHsznHWfbK3wY5bk2kDjjsaaaVNlNVIWl52tPpHOrWAaca0uaMVLWuM6IP1tdiWsFI%3D'
        to_sign1   = '__method=getDomainNames&__service=DomainService&__hostname=api.transip.nl&__timestamp=1390235362&__nonce=2e49613c-35b9-4827-a882-8d755504'

        reference2 = 'ly2K%2BZjs45hMqTsF%2BxwwHeTvqlHHchvLkRokP16EISaukSkOf714bA0QJA7QxipxPQEHyWNoezD5g3vb2OWv38N8U%2BFLGbcpoT89hi2Zsv7B96QBcew8cxvgwdBM0rM8ixYuw%2FyASsG%2BLvyEzo55eXE3st2aAsG5CP1xwQdLG0I%3D'
        to_sign2   = '__method=getDomainNames&__service=DomainService&__hostname=api.transip.nl&__timestamp=1390236369&__nonce=e0736a8f-fcf4-435f-a7f1-c1d2ccaa'

        c = Client('foo')
        c.private_file = 'test_key'

        # CALL
        signature1 = c._sign(to_sign1)
        signature2 = c._sign(to_sign2)

        # VERIFY
        self.assertEqual(signature1, reference1)
        self.assertEqual(signature2, reference2)

    @patch('suds.client.Client')
    def testBuildSignature(self, mock_client):
        # SETUP
        c = Client('foo')
        reference = '__method=getDomainNames&__service=DomainService&__hostname=api.transip.nl&__timestamp=123&__nonce=TEST-NONCE'

        # CALL
        message = c._build_signature_message('DomainService', 'getDomainNames', 123, 'TEST-NONCE')

        # VERIFY
        self.assertEqual(message, reference)

    @patch('uuid.uuid4')
    @patch('time.time')
    @patch('suds.client.Client')
    def testBuildCookies(self, mock_client, mock_time, mock_uuid):
        # SETUP
        c = Client('DomainService')
        c.private_file = 'test_key'

        mock_uuid.return_value = '2e49613c-35b9-4827-a882-8d755504'
        mock_time.return_value = 1390235362

        reference_cookie = {
            'login': 'sundayafternoon',
            'mode': MODE_RO,
            'timestamp': 1390235362,
            'nonce': '2e49613c-35b9-4827-a882-8d755504',
            'clientVersion': transip.__version__,
            'signature':'ZurqqM1HQTWqYb5IOFYEk%2BGw7a2I%2FknIHEw9lJag%2FnHDp3XfZYj%2F89GTjM52x6spJEJtUnUpSZ02DsVoaJlGl4iZEMk0%2FbWcP5ODRJhASHHsznHWfbK3wY5bk2kDjjsaaaVNlNVIWl52tPpHOrWAaca0uaMVLWuM6IP1tdiWsFI%3D'
        }

        # CALL
        cookie = c.build_cookie(mode = 'readonly', method = 'getDomainNames')

        # VERIFY
        self.maxDiff = None
        self.assertEqual(cookie, reference_cookie)


    @patch('suds.xsd.doctor.ImportDoctor')
    @patch('suds.xsd.doctor.Import')
    @patch('suds.client.Client')
    def testSoapClientIsInitialised(self, mock_client, mock_import, mock_import_doctor):
        # SETUP
        c = Client('DomainService')

        # VERIFY
        self.assertEqual(c.soap_client, mock_client())

    @patch('suds.client.Client')
    def testUpdateCookie(self, mock_client):
        # SETUP
        c = Client('Foo')

        cookie = {
            'foo' : 'bar',
            'baz' : 'qux'
        } 

        # CALL
        c.update_cookie(cookie)
        # VERIFY
        c.soap_client.set_options.assert_called_with(headers={'Cookie': 'foo=bar;baz=qux'})





    
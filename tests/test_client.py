# vim: set fileencoding=utf-8 :
import unittest
from mock import patch, Mock

import transip
from transip.client import Client, MODE_RO


class TestClient(unittest.TestCase):

    @patch('transip.client.SudsClient')
    def testConstructor(self, mock_client):
        # CALL
        c = Client('TestService', login='sundayafternoon')

        # VERIFY
        self.assertEqual(c.service_name, 'TestService')
        self.assertEqual(c.url, 'https://api.transip.nl/wsdl/?service=TestService')

    @patch('transip.client.SudsClient')
    def testSignatureIsCorrect(self, mock_client):
        # SETUP
        reference1 = 'ZurqqM1HQTWqYb5IOFYEk%2BGw7a2I%2FknIHEw9lJag%2FnHDp3XfZYj%2F89GTjM52x6spJEJtUnUpSZ02DsVoaJlGl4iZEMk0%2FbWcP5ODRJhASHHsznHWfbK3wY5bk2kDjjsaaaVNlNVIWl52tPpHOrWAaca0uaMVLWuM6IP1tdiWsFI%3D'
        to_sign1   = '__method=getDomainNames&__service=DomainService&__hostname=api.transip.nl&__timestamp=1390235362&__nonce=2e49613c-35b9-4827-a882-8d755504'

        reference2 = 'ly2K%2BZjs45hMqTsF%2BxwwHeTvqlHHchvLkRokP16EISaukSkOf714bA0QJA7QxipxPQEHyWNoezD5g3vb2OWv38N8U%2BFLGbcpoT89hi2Zsv7B96QBcew8cxvgwdBM0rM8ixYuw%2FyASsG%2BLvyEzo55eXE3st2aAsG5CP1xwQdLG0I%3D'
        to_sign2   = '__method=getDomainNames&__service=DomainService&__hostname=api.transip.nl&__timestamp=1390236369&__nonce=e0736a8f-fcf4-435f-a7f1-c1d2ccaa'

        c = Client('foo', login='sundayafternoon', private_key_file='test_key')

        # CALL
        signature1 = c._sign(to_sign1)
        signature2 = c._sign(to_sign2)

        # VERIFY
        self.assertEqual(signature1, reference1)
        self.assertEqual(signature2, reference2)

    @patch('transip.client.SudsClient')
    def testBuildSignature(self, mock_client):
        # SETUP
        c = Client('foo', login='sundayafternoon')
        reference = '__method=getDomainNames&__service=DomainService&__hostname=api.transip.nl&__timestamp=123&__nonce=TEST-NONCE'

        # CALL
        message = c._build_signature_message('DomainService', 'getDomainNames', 123, 'TEST-NONCE')

        # VERIFY
        self.assertEqual(message, reference)

    @patch('transip.client.SudsClient')
    def testBuildSignatureWithAdditionalParameters(self, mock_client):
        # SETUP
        c = Client('foo', login='sundayafternoon')
        reference = '0=foo&1=bar&__method=getDomainNames&__service=DomainService&__hostname=api.transip.nl&__timestamp=123&__nonce=TEST-NONCE'

        additional = ['foo', 'bar']

        # CALL
        message = c._build_signature_message('DomainService', 'getDomainNames', 123, 'TEST-NONCE', additional)

        # VERIFY
        self.assertEqual(message, reference)

    @patch('transip.client.SudsClient')
    def testBuildSignatureParametersSpecialCharacters(self, mock_client):
        # SETUP
        c = Client('foo', login='sundayafternoon')
        reference = '0=foo%20bar&1=~all&2=%2A.foo&__method=getDomainNames&__service=DomainService&__hostname=api.transip.nl&__timestamp=123&__nonce=TEST-NONCE'

        additional = ['foo bar', '~all', '*.foo']

        # CALL
        message = c._build_signature_message('DomainService', 'getDomainNames', 123, 'TEST-NONCE', additional)

        # VERIFY
        self.assertEqual(message, reference)

    @patch('uuid.uuid4')
    @patch('time.time')
    @patch('transip.client.SudsClient')
    def testBuildCookies(self, mock_client, mock_time, mock_uuid):
        # SETUP
        c = Client('DomainService', login='sundayafternoon', private_key_file='test_key')

        mock_uuid.return_value = 'MOCKED-NONCE'
        mock_time.return_value = 123

        c._sign = Mock()
        c._sign.return_value = "MOCKED-SIGNATURE"

        reference_cookie = {
            'login': 'sundayafternoon',
            'mode': MODE_RO,
            'timestamp': 123,
            'nonce': 'MOCKED-NONCE',
            'clientVersion': transip.__version__,
            'signature':'MOCKED-SIGNATURE'
        }

        # CALL
        cookie = c.build_cookie(mode='readonly', method='getDomainNames')

        # VERIFY
        self.maxDiff = None
        self.assertEqual(cookie, reference_cookie)
        c._sign.assert_called_with('__method=getDomainNames&__service=DomainService&__hostname=api.transip.nl&__timestamp=123&__nonce=MOCKED-NONCE')

    @patch('uuid.uuid4')
    @patch('time.time')
    @patch('transip.client.SudsClient')
    def testBuildCookiesWithAdditionalParameters(self, mock_client, mock_time, mock_uuid):
        # SETUP
        c = Client('DomainService', login='sundayafternoon', private_key_file='test_key')

        c._sign = Mock()
        c._sign.return_value = "MOCKED-SIGNATURE"

        mock_uuid.return_value = 'MOCKED-NONCE'
        mock_time.return_value = 123

        reference_cookie = {
            'login': 'sundayafternoon',
            'mode': MODE_RO,
            'timestamp': 123,
            'nonce': 'MOCKED-NONCE',
            'clientVersion': transip.__version__,
            'signature':'MOCKED-SIGNATURE'
        }

        # CALL
        cookie = c.build_cookie(mode = 'readonly', method = 'getInfo', parameters=['example.com'])

        # VERIFY
        self.maxDiff = None
        self.assertEqual(cookie, reference_cookie)
        c._sign.assert_called_with('0=example.com&__method=getInfo&__service=DomainService&__hostname=api.transip.nl&__timestamp=123&__nonce=MOCKED-NONCE')

    @patch('transip.client.ImportDoctor')
    @patch('transip.client.Import')
    @patch('transip.client.SudsClient')
    def testSoapClientIsInitialised(self, mock_client, mock_import, mock_import_doctor):
        # SETUP
        c = Client('DomainService', login='loginname')

        # VERIFY
        self.assertEqual(c.soap_client, mock_client())

    @patch('transip.client.SudsClient')
    def testUpdateCookie(self, mock_client):
        # SETUP
        c = Client('Foo', login='sundayafternoon')

        cookie = {
            'foo': 'bar',
            'baz': 'qux'
        } 

        # CALL
        c.update_cookie(cookie)
        # VERIFY
        c.soap_client.set_options.assert_called_with(headers={'Cookie': 'foo=bar;baz=qux'})


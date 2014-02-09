import unittest
import mock
from mock import patch

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
        reference1 = 'OkWhzVgYPeERy1ItxUHr31A%2F80MQlo75VkJLCSwmZ2xbIyUXrx2S%2BSwNJfJT3r3t8PQzya04r5RqhXxqezMlDfGHALxQ24GgMCl8iGjTfNoSDSuoTCA78AzfVbESN5jXWixvTdfiQRyiaPbv6CGpQ6jDw1nU6yEvchzIzMT%2FuO5y9gHA%2FKpx0W7JHR9x2J1QMq7CRj3GE2n9ASrwyKDzem2M%2F592c5WURAtjReUI00Wks3egl5gquwtg91I78qHu%2Fnbv06JJVQalPpKFerHhBp%2BL6ZGxObX%2BRHTofwXuiCIC911lgyz6xXKz0u2%2FLzVLAykU7W3XXIIDP58Eym3LUA%3D%3D'
        to_sign1   = '__method=getDomainNames&__service=DomainService&__hostname=api.transip.nl&__timestamp=1390235362&__nonce=2e49613c-35b9-4827-a882-8d755504'

        reference2 = 'brraypeNe2GlIW3xUJLRlOigk534UVIe3iSFdYcHvV2a3D26Q%2F94rL415KTrnd3ayFff7CgJY%2FV0aJVnBGUJQCcEyW3GAdVN54MNm4FKzsSqVThUHyIVZBkhl2uQMS0FpnpMGecRbnytptaIW2o6G1itTYjuMpYbqZS9zfpHGe3Aui3p%2FmqiRxpiBsTTNCXvE0sSHY%2F08XdGU0vM40%2BaQJ51C7b08GIWYtoYYD1AVbwPFo3c8C3LQ0IAXTjtwe5Bf2y5L9xAKauXttVrljKyQsscTfayNPYfRjXLsoO0DybhOTXLV4unEXpm523mMNSXFZOCcNxdhpj2gfQsDVgbcA%3D%3D'
        to_sign2   = '__method=getDomainNames&__service=DomainService&__hostname=api.transip.nl&__timestamp=1390236369&__nonce=e0736a8f-fcf4-435f-a7f1-c1d2ccaa'

        c = Client('foo')

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
    def testBuildCookies(self, mock_time, mock_uuid):
        # SETUP
        c = Client('DomainService')

        mock_uuid.return_value = '2e49613c-35b9-4827-a882-8d755504'
        mock_time.return_value = 1390235362

        reference_cookie = {
            'login': 'sundayafternoon',
            'mode': MODE_RO,
            'timestamp': 1390235362,
            'nonce': '2e49613c-35b9-4827-a882-8d755504',
            'clientVersion': transip.__version__,
            'signature':'OkWhzVgYPeERy1ItxUHr31A%2F80MQlo75VkJLCSwmZ2xbIyUXrx2S%2BSwNJfJT3r3t8PQzya04r5RqhXxqezMlDfGHALxQ24GgMCl8iGjTfNoSDSuoTCA78AzfVbESN5jXWixvTdfiQRyiaPbv6CGpQ6jDw1nU6yEvchzIzMT%2FuO5y9gHA%2FKpx0W7JHR9x2J1QMq7CRj3GE2n9ASrwyKDzem2M%2F592c5WURAtjReUI00Wks3egl5gquwtg91I78qHu%2Fnbv06JJVQalPpKFerHhBp%2BL6ZGxObX%2BRHTofwXuiCIC911lgyz6xXKz0u2%2FLzVLAykU7W3XXIIDP58Eym3LUA%3D%3D'
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





    
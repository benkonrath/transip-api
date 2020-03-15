"""
The Client class, handling direct communication with the API
"""

from __future__ import print_function

import base64
import os
import time
import uuid
from collections import OrderedDict

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from suds.client import Client as SudsClient
from suds.sudsobject import Object as SudsObject
from suds.xsd.doctor import Import, ImportDoctor
from suds.plugin import DocumentPlugin

from . import __version__

try:
    from urllib.parse import urlencode, quote_plus
except ImportError:
    from urllib import urlencode, quote_plus

try:
    import suds_requests
except ImportError:
    suds_requests = None


URI_TEMPLATE = 'https://{}/wsdl/?service={}'

MODE_RO = 'readonly'
MODE_RW = 'readwrite'


def convert_value(value):
    """
    None and boolean values are not accepted by the Transip API.
    This method converts
        - None and False to an empty string,
        - True to 1
    """
    if isinstance(value, bool):
        return 1 if value else ''

    if not value:
        return ''

    return value

class WSDLFixPlugin(DocumentPlugin):
    # pylint: disable=W0232
    """
    A SudsFilter to fix wsdl document before it is parsed.
    """

    def loaded(self, context):
        # pylint: disable=R0201
        """
        Replaces an invalid type in the wsdl document with a validy type.
        """
        context.document = context.document.replace(b'xsd:array', b'soapenc:Array')

class Client(object):
    """
    A client-base class, for other classes to base their service implementation
    on. Contains methods to set and sign cookie and to retrieve the correct
    WSDL for specific parts of the TransIP API.

    Note:
        You either need to supply a private_key or a private_key_file.

    Args:
        service_name (str): Name of the service.
        login (str): The TransIP username.
        private_key (str, optional): The content of the private key for
            accessing the TransIP API.
        private_key_file (str, optional): Path the the private key for
            accesing the TransIP API. Defaults to 'decrypted_key'.
        endpoint (str): The TransIP API endpoint. Defaults to 'api.transip.nl'.
    """
    def __init__(self, service_name, login, private_key=None,
                 private_key_file='decrypted_key', endpoint='api.transip.nl'):
        self.service_name = service_name
        self.login = login
        self.private_key = private_key
        self.private_key_file = private_key_file
        self.endpoint = endpoint
        self.url = URI_TEMPLATE.format(endpoint, service_name)

        imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
        doc = ImportDoctor(imp)

        suds_kwargs = dict()
        if suds_requests:
            suds_kwargs['transport'] = suds_requests.RequestsTransport()

        self.soap_client = SudsClient(self.url, doctor=doc, plugins=[WSDLFixPlugin()], **suds_kwargs)

    def _sign(self, message):
        """ Uses the decrypted private key to sign the message. """
        if self.private_key:
            keydata = self.private_key
        elif os.path.exists(self.private_key_file):
            with open(self.private_key_file) as private_key:
                keydata = private_key.read()
        else:
            raise RuntimeError('The private key does not exist.')

        private_key = serialization.load_pem_private_key(
            str.encode(keydata),
            password=None,
            backend=default_backend()
        )
        signature = private_key.sign(
            str.encode(message),
            padding.PKCS1v15(),
            hashes.SHA512(),
        )

        signature = base64.b64encode(signature)
        signature = quote_plus(signature)

        return signature

    def _build_signature_message(self, service_name, method_name,
                                 timestamp, nonce, additional=None):
        """
        Builds the message that should be signed. This message contains
        specific information about the request in a specific order.
        """
        if additional is None:
            additional = []

        sign = OrderedDict()
        # Add all additional parameters first
        for index, value in enumerate(additional):
            if isinstance(value, list):
                for entryindex, entryvalue in enumerate(value):
                    if isinstance(entryvalue, SudsObject):
                        for objectkey, objectvalue in entryvalue:
                            objectvalue = convert_value(objectvalue)
                            sign[str(index) + '[' + str(entryindex) + '][' + objectkey + ']'] = objectvalue
            elif isinstance(value, SudsObject):
                for entryindex, entryvalue in value:
                    key = str(index) + '[' + str(entryindex) + ']'
                    sign[key] = convert_value(entryvalue)
            else:
                sign[index] = convert_value(value)
        sign['__method'] = method_name
        sign['__service'] = service_name
        sign['__hostname'] = self.endpoint
        sign['__timestamp'] = timestamp
        sign['__nonce'] = nonce

        return urlencode(sign) \
            .replace('%5B', '[') \
            .replace('%5D', ']') \
            .replace('+', '%20') \
            .replace('%7E', '~')  # Comply with RFC3989. This replacement is also in TransIP's sample PHP library.

    def update_cookie(self, cookies):
        """ Updates the cookie for the upcoming call to the API. """
        temp = []
        for k, val in cookies.items():
            temp.append("%s=%s" % (k, val))

        cookiestring = ';'.join(temp)
        self.soap_client.set_options(headers={'Cookie': cookiestring})

    def build_cookie(self, method, mode, parameters=None):
        """
        Build a cookie for the request.

        Keyword arguments:
        method -- the method to be called on the service.
        mode -- Read-only (MODE_RO) or read-write (MODE_RW)
        """
        timestamp = int(time.time())
        nonce = str(uuid.uuid4())[:32]

        message_to_sign = self._build_signature_message(
            service_name=self.service_name,
            method_name=method,
            timestamp=timestamp,
            nonce=nonce,
            additional=parameters
        )

        signature = self._sign(message_to_sign)

        cookies = {
            "nonce": nonce,
            "timestamp": timestamp,
            "mode": mode,
            "clientVersion": __version__,
            "login": self.login,
            "signature": signature
        }

        return cookies

    def _simple_request(self, method, *args, **kwargs):
        """
        Helper method to create a request in a DRY way
        """
        cookie = self.build_cookie(mode=kwargs.get('mode', MODE_RO), method=method, parameters=args)
        self.update_cookie(cookie)

        return getattr(self.soap_client.service, method)(*args)

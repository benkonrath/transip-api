"""
The Client class, handling direct communication with the API
"""

import rsa
import uuid
import time
import base64
import urllib

from . import __version__

from collections import OrderedDict
# from urimagic import percent_encode

import suds
from suds.xsd.doctor import ImportDoctor, Import
from suds.sudsobject import Object as SudsObject


URI_TEMPLATE = "https://api.transip.nl/wsdl/?service={}"

MODE_RO = 'readonly'
MODE_RW = 'readwrite'

class Client(object):
    """
    A client-base class, for other classes to base their service implementation
    on. Contains methods to set and sign cookie and to retrieve the correct
    WSDL for specific parts of the TransIP API.
    """

    login = 'sundayafternoon'
    endpoint = 'api.transip.nl'
    private_file = 'decrypted_key'
    service_name = None
    soap_client = None
    url = None

    def __init__(self, service_name):
        """ Initialiser. """
        self.service_name = service_name
        self.url = URI_TEMPLATE.format(self.service_name)
        self._init_soap_client()


    def _sign(self, message):
        """ Uses the decrypted private key to sign the message. """
        signature = None
        with open(self.private_file) as private_key:
            keydata = private_key.read()
            privkey = rsa.PrivateKey.load_pkcs1(keydata)
            signature = rsa.sign(message, privkey, 'SHA-512')
            signature = base64.b64encode(signature)
            signature = urllib.quote_plus(signature)

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
                            sign[str(index)+'['+str(entryindex)+']['+objectkey+']'] = objectvalue
            else:
                sign[index] = value
        sign['__method'] = method_name
        sign['__service'] = service_name
        sign['__hostname'] = self.endpoint
        sign['__timestamp'] = timestamp
        sign['__nonce'] = nonce

        return urllib.urlencode(sign).replace('%5B', '[').replace('%5D', ']').replace('+', '%20')

    def update_cookie(self, cookies):
        """ Updates the cookie for the upcoming call to the API. """
        temp = []
        for k, val in cookies.items():
            temp.append("%s=%s"%(k, val))

        cookiestring = ';'.join(temp)
        self.soap_client.set_options(headers={'Cookie' : cookiestring})

    def build_cookie(self, method, mode, parameters=None):
        """
        Build a cookie for the request.

        Keword arguments:
        method -- the method to be called on the service.
        mode -- Read-only (MODE_RO) or read-write (MODE_RW)
        """
        timestamp = int(time.time())
        nonce = str(uuid.uuid4())[:32]

        signature = self._sign(self._build_signature_message(
            service_name=self.service_name, method_name=method,
            timestamp=timestamp, nonce=nonce, additional=parameters))

        cookies = {
            "nonce"         : nonce,
            "timestamp"     : timestamp,
            "mode"          : mode,
            "clientVersion" : __version__,
            "login"         : self.login,
            "signature"     : signature
        }

        return cookies


    def _init_soap_client(self):
        """ Initialises the suds soap-client """
        imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
        doc = ImportDoctor(imp)
        self.soap_client = suds.client.Client(self.url, doctor=doc)

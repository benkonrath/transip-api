import base64
import time
import uuid
import rsa
import urllib
from collections import OrderedDict
from urimagic import percent_encode

from pprint import pprint

from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import

import logging
logging.basicConfig(level=logging.INFO)

logging.getLogger('suds.client').setLevel(logging.DEBUG)


def main():

	serviceName = 'DomainService'
	url         = 'https://api.transip.nl/wsdl/?service=%s' % serviceName
	endpoint    = 'api.transip.nl'
	timestamp   = int(time.time())
	nonce       = str(uuid.uuid4())[:32]

	cookies = {
		"nonce"    : nonce,
		"timestamp": timestamp,
		"mode"     : "readonly",
		"login"    : "sundayafternoon"
	}

	sign = OrderedDict()
	sign['__method']    = 'getDomainNames'
	sign['__service']   = serviceName
	sign['__hostname']  = endpoint
	sign['__timestamp'] = timestamp
	sign['__nonce']     = nonce


	mesg = urllib.urlencode(sign)
	print("TO SIGN: {}".format(mesg))
	signature = ''
	with open('decrypted') as encrypted_privatefile:
		keydata = encrypted_privatefile.read()
		privkey = rsa.PrivateKey.load_pkcs1(keydata)
		signature = rsa.sign(mesg, privkey, 'SHA-512')
		signature = base64.b64encode(signature)
		signature = urllib.quote_plus(signature)

	cookies['signature'] = signature;


	foo = []
	for k,v in cookies.items():
		foo.append("%s=%s"%(k,v))

	cookiestring = ';'.join(foo)


	

	cookiestring = "%s;signature=%s" % (cookiestring, signature)

	headers = { 'Cookie' : cookiestring }
	
	imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
	d = ImportDoctor(imp)
	client = Client(url, doctor=d, headers=headers)

	dn = client.service.getDomainNames()
	print(dn)


if __name__ == '__main__':
	main()
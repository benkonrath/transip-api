""" The CLI parser for the API """

from transip.service.domain import DomainService

# from pprint import pprint

import logging
logging.basicConfig(level=logging.INFO)

logging.getLogger('suds.client').setLevel(logging.DEBUG)


def main():
    """ The main method """
    domain_service = DomainService()
    # cookies = domain_service.build_cookie(mode = MODE_RO,
        # method= 'getDomainNames')

    # foo = []
    # for k,v in cookies.items():
    #   foo.append("%s=%s"%(k,v))

    # cookiestring = ';'.join(foo)


    # headers = { 'Cookie' : cookiestring }
    # print (headers)


    # imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
    # d = ImportDoctor(imp)
    # client = Client(domain_service.url, doctor=d, headers=headers)

    # dn = client.service.getDomainNames()

    names = domain_service.get_domain_names()
    print names


if __name__ == '__main__':
    main()

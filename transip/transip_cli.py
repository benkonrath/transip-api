"""
The CLI parser for the API
"""

from transip.service.domain import DomainService
# from pprint import pprint

import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.INFO)


def main():
    """ The main method """
    domain_service = DomainService()
    names = domain_service.get_domain_names()
    print names


if __name__ == '__main__':
    main()

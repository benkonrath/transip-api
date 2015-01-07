"""
The CLI parser for the API
"""
from __future__ import print_function

import argparse
from suds import WebFault

from transip.service.dns import DnsEntry
from transip.service.domain import DomainService
# from pprint import pprint

import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.INFO)


def update_dns_entry(domain_service, args):
    """
    Updates a DNS entry through the API
    :param domain_service: a DomainService object
    :param args: arguments object from argparse
    """
    if args.entry_domain and args.entry_name and args.entry_expire and args.entry_type and args.entry_content:
        try:
            dns_entries = domain_service.get_info(args.entry_domain).dnsEntries
        except WebFault as err:
            print(err)
            exit(1)
        for entry in dns_entries:
            if entry.name == args.entry_name and entry.type == args.entry_type:
                dns_entries.remove(entry)
        dns_entries.append(DnsEntry(args.entry_name, args.entry_expire, args.entry_type, args.entry_content))
        try:
            result = domain_service.set_dns_entries(args.entry_domain, dns_entries)
        except WebFault as err:
            print(err)
            exit(1)
        if result is None:
            print('Request finished successfully.')
        else:
            print(result)
    else:
        print('Please provide the details of the DNS entry.')
        exit(1)


def main():
    """ The main method """
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--login-name', help='TransIP username', dest='loginname')
    parser.add_argument('-u', '--update-dns-entry', help='add or update an entry in the DNS', action='store_true')
    parser.add_argument('--entry-domain', help='domain name to update the entry in', dest='entry_domain')
    parser.add_argument('--entry-name', help='name of the DNS entry', dest='entry_name')
    parser.add_argument('--entry-expire', help='expire time of the DNS entry', dest='entry_expire', type=int)
    parser.add_argument('--entry-type', help='type of the DNS entry', dest='entry_type')
    parser.add_argument('--entry-content', help='content of the DNS entry', dest='entry_content')
    args = parser.parse_args()

    if not args.loginname:
        print('Please provide your TransIP username.')
        exit(1)

    domain_service = DomainService()
    domain_service.login = args.loginname

    if args.update_dns_entry:
        update_dns_entry(domain_service, args)
    else:
        names = domain_service.get_domain_names()
        print(names)


if __name__ == '__main__':
    main()

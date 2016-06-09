"""
The CLI parser for the API
"""
from __future__ import print_function

import argparse
import logging

from suds import WebFault

from transip.service.dns import DnsEntry
from transip.service.domain import DomainService

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.INFO)


def show_dns_entries(domain_service, domain_name):
    """
    Lists all DNS entries for the provided domain name
    :param domain_service: an initialized DomainService object
    :param domain_name: domain name
    :return:
    """
    try:
        dns_entries = domain_service.get_info(domain_name).dnsEntries
    except WebFault as err:
        print(err)
        exit(1)
    print(dns_entries)


def update_dns(domain_service, args):
    """
    Adds, updates or deletes a DNS entry through the API
    :param domain_service: an initialized DomainService object
    :param args: arguments object from argparse
    """

    try:
        dns_entries = domain_service.get_info(args.domain_name).dnsEntries
    except WebFault as err:
        print(err)
        exit(1)
    amount_of_entries = len(dns_entries)
    for entry in dns_entries:
        if args.add_dns_entry and entry.name == args.entry_name and entry.type == args.entry_type and \
                        entry.content == args.entry_content:
            print('The DNS entry already exists.')
            exit(1)
        if args.update_dns_entry and entry.name == args.entry_name and entry.type == args.entry_type:
            dns_entries.remove(entry)
        if args.delete_dns_entry and entry.name == args.entry_name and entry.type == args.entry_type and \
                        entry.expire == args.entry_expire and entry.content == args.entry_content:
            dns_entries.remove(entry)
    if args.update_dns_entry or args.delete_dns_entry:
        if amount_of_entries == len(dns_entries):
            print('The DNS entry was not found.')
            exit(1)
    if args.add_dns_entry or args.update_dns_entry:
        dns_entries.append(DnsEntry(args.entry_name, args.entry_expire, args.entry_type, args.entry_content))
    try:
        result = domain_service.set_dns_entries(args.domain_name, dns_entries)
    except WebFault as err:
        print(err)
        exit(1)
    if result is None:
        print('Request finished successfully.')
    else:
        print(result)


def main():
    """ The main method """
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--login-name', help='TransIP username', dest='loginname')
    parser.add_argument('-s', '--show-dns-entries', help='show all DNS entries for a domain', action='store_true')
    parser.add_argument('-a', '--add-dns-entry', help='add an entry in the DNS', action='store_true')
    parser.add_argument('-u', '--update-dns-entry', help='update an entry in the DNS', action='store_true')
    parser.add_argument('-d', '--delete-dns-entry', help='delete an entry in the DNS', action='store_true')
    parser.add_argument('--domain-name', help='domain name to use', dest='domain_name')
    parser.add_argument('--entry-name', help='name of the DNS entry', dest='entry_name')
    parser.add_argument('--entry-expire', help='expire time of the DNS entry', dest='entry_expire', type=int)
    parser.add_argument('--entry-type', help='type of the DNS entry', dest='entry_type')
    parser.add_argument('--entry-content', help='content of the DNS entry', dest='entry_content')
    args = parser.parse_args()

    if not args.loginname:
        print('Please provide your TransIP username.')
        exit(1)

    domain_service = DomainService(args.loginname)

    if args.add_dns_entry or args.update_dns_entry or args.delete_dns_entry:
        if args.domain_name and args.entry_name and args.entry_expire and args.entry_type and args.entry_content:
            update_dns(domain_service, args)
        else:
            print('Please provide the details of the DNS entry.')
            exit(1)
    elif args.show_dns_entries:
        if args.domain_name:
            show_dns_entries(domain_service, args.domain_name)
        else:
            print('Please provide the domain name.')
            exit(1)
    else:
        names = domain_service.get_domain_names()
        print(names)


if __name__ == '__main__':
    main()

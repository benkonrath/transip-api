""" The connector to Domain related API calls """

from transip.client import Client, MODE_RO, MODE_RW

class DomainService(Client):
    """ Representation of the DomainService API calls for TransIP """

    def __init__(self):
        Client.__init__(self, 'DomainService')

    def get_domain_names(self):
        """
            Retrieves a list of all domains currently available
            for this account.
        """
        cookie = self.build_cookie(mode=MODE_RO, method='getDomainNames')
        self.update_cookie(cookie)

        return self.soap_client.service.getDomainNames()

    def get_info(self, domain_name):
        """Retrieves information about the requested domain-name."""

        cookie = self.build_cookie(mode=MODE_RO, method='getInfo', parameters=[domain_name])
        self.update_cookie(cookie)

        return self.soap_client.service.getInfo(domain_name)

    def set_dns_entries(self, domain_name, dns_entries):
        """
        Sets the DnEntries for this Domain, will replace ALL existing dns entries with the new entries

        :param domain_name: the domainName to change the dns entries for
        :param dns_entries: the list of ALL DnsEntries for this domain
        :type domain_name: basestring
        :type dns_entries: list
        """
        cookie = self.build_cookie(mode=MODE_RW, method='setDnsEntries', parameters=[domain_name, dns_entries])
        self.update_cookie(cookie)

        return self.soap_client.service.setDnsEntries(domain_name, dns_entries)

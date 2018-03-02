# pylint: disable=too-many-public-methods
""" The connector to Domain related API calls """

from transip.client import Client, MODE_RO, MODE_RW
from transip.service.objects import DnsEntry


class DomainService(Client):
    """ Representation of the DomainService API calls for TransIP """

    def __init__(self, *args, **kwargs):
        super(DomainService, self).__init__('DomainService', *args, **kwargs)

    def batch_check_availability(self, domain_names):
        """
        Transip_DomainService::batchCheckAvailability
        Allows only 20 domain names per request
        :type domain_names: list of str
        :rtype: list of transip.service.objects.DomainCheckResult
        """

        if len(domain_names) > 20:
            raise ValueError('There is a maximum of 20 domain names per request.')

        return self._simple_request('batchCheckAvailability', domain_names)

    def check_availability(self, domain_name):
        """
        Transip_DomainService::checkAvailability
        :type domain_name: str
        :rtype: str the availability status of the domain name
        """
        return self._simple_request('checkAvailability', domain_name)

    def get_whois(self, domain_name):
        """
        Transip_DomainService::getWhois
        :type domain_name: str
        :rtype: str
        """
        return self._simple_request('getWhois', domain_name)

    def get_domain_names(self):
        """
        Transip_DomainService::getDomainNames
        :rtype: list of str
        """
        return self._simple_request('getDomainNames')

    def get_info(self, domain_name):
        """
        Retrieves information about the requested domain-name.
        :param domain_name: str
        :rtype: transip.service.objects.Domain
        """
        cookie = self.build_cookie(mode=MODE_RO, method='getInfo', parameters=[domain_name])
        self.update_cookie(cookie)

        # Perform the call
        result = self.soap_client.service.getInfo(domain_name)

        # Parse the result to well-known objects
        new_dns_entries = []
        for dnsentry in result.dnsEntries:
            if dnsentry.__class__.__name__ == 'DnsEntry':
                new_dns_entries.append(DnsEntry(dnsentry.name, dnsentry.expire, dnsentry.type, dnsentry.content))
        result.dnsEntries = new_dns_entries

        return result

    def batch_get_info(self, domain_names):
        """
        Transip_DomainService::batchGetInfo
        :type domain_names: list of str
        :rtype: list of transip.service.objects.Domain
        """
        return self._simple_request('batchGetInfo', domain_names)

    def get_auth_code(self, domain_name):
        """
        Transip_DomainService::getAuthCode
        :type domain_name: str
        :rtype: str
        """
        return self._simple_request('getAuthCode', domain_name)

    def get_is_locked(self, domain_name):
        """
        Transip_DomainService::getIsLocked (@deprecated use getInfo)
        :type domain_name: str
        :rtype: bool
        """
        return self._simple_request('getIsLocked', domain_name)

    def register(self, domain):
        """
        Transip_DomainService::register
        :type domain: transip.service.object.Domain
        """
        return self._simple_request('register', domain, mode=MODE_RW)

    def cancel(self, domain_name, end_time):
        """
        Transip_DomainService::batchGetInfo
        :type domain_name: str
        :type end_time: datetime.datetime
        """
        return self._simple_request('cancel', domain_name, end_time, mode=MODE_RW)

    def transfer_with_owner_change(self, domain, auth_code):
        """
        Transip_DomainService::transferWithOwnerChange
        :type domain: transip.service.objects.Domain
        :type auth_code: str
        """
        return self._simple_request('transferWithOwnerChange', domain, auth_code, mode=MODE_RW)

    def transfer_without_owner_change(self, domain, auth_code):
        """
        Transip_DomainService::transferWithoutOwnerChange
        :type domain: transip.service.objects.Domain
        :type auth_code: str
        """
        return self._simple_request('transferWithoutOwnerChange', domain, auth_code, mode=MODE_RW)

    def set_nameservers(self, domain_name, nameservers):
        """
        Transip_DomainService::batchGetInfo
        :type domain_name: str
        :type nameservers: list of transip.service.objects.Nameserver
        """
        return self._simple_request('setNameservers', domain_name, nameservers, mode=MODE_RW)

    def set_lock(self, domain_name):
        """
        Transip_DomainService::batchGetInfo
        :type domain_name: str
        """
        return self._simple_request('setLock', domain_name, mode=MODE_RW)

    def unset_lock(self, domain_name):
        """
        Transip_DomainService::batchGetInfo
        """
        return self._simple_request('unsetLock', domain_name, mode=MODE_RW)

    def set_dns_entries(self, domain_name, dns_entries):
        """
        Sets the DnEntries for this Domain, will replace ALL existing dns entries with the new entries
        :type domain_name: str
        :type dns_entries: list of transip.service.objects.DnsEntry
        """
        return self._simple_request('setDnsEntries', domain_name, dns_entries, mode=MODE_RW)

    def set_owner(self, domain_name, registrant_whois_contact):
        """
        Transip_DomainService::batchGetInfo
        :type domain_name: str
        :type registrant_whois_contact: transip.service.objects.WhoisContact
        """
        return self._simple_request('setOwner', domain_name, registrant_whois_contact, mode=MODE_RW)

    def set_contacts(self, domain_name, contacts):
        """
        Transip_DomainService::setContacts
        :type domain_name: str
        :type contacts: list of transip.service.objects.WhoisContact
        """
        return self._simple_request('setContacts', domain_name, contacts, mode=MODE_RW)

    def get_all_tld_infos(self):
        """
        Transip_DomainService::batchGetInfo
        :rtype: list of transip.service.objects.Tld
        """
        return self._simple_request('getAllTldInfos')

    def get_tld_info(self, tld_name):
        """
        Transip_DomainService::getTldInfo
        :type tld_name: str
        :rtype: transip.service.objects.Tld
        """
        return self._simple_request('getTldInfo', tld_name)

    def get_current_domain_action(self, domain_name):
        """
        Transip_DomainService::getCurrentDomainAction
        :type domain_name: str
        :rtype: transip.service.objects.DomainAction
        """
        return self._simple_request('getCurrentDomainAction', domain_name)

    def retry_current_domain_action_with_new_data(self, domain):  # pylint: disable=invalid-name,locally-disabled
        """
        Transip_DomainService::retryCurrentDomainActionWithNewData
        :type domain: transip.service.objects.Domain
        """
        return self._simple_request('retryCurrentDomainActionWithNewData', domain)

    def retry_transfer_with_different_auth_code(self, domain, new_auth_code):  # pylint: disable=invalid-name,locally-disabled
        """
        Transip_DomainService::retryTransferWithDifferentAuthCode
        :param domain: transip.service.objects.Domain
        :type new_auth_code: str
        """
        return self._simple_request('retryTransferWithDifferentAuthCode', domain, new_auth_code)

    def cancel_domain_action(self, domain):
        """
        Transip_DomainService::cancelDomainAction
        :type domain: transip.service.objects.Domain
        """
        return self._simple_request('cancelDomainAction', domain)

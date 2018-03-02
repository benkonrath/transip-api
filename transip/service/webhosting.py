"""
Implementation of the WebhostingService API endpoint
"""
from transip.client import Client, MODE_RW


class WebhostingService(Client):
    """
    Transip_WebhostingService
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        super(WebhostingService, self).__init__('WebhostingService', *args, **kwargs)

    def get_webhosting_domain_names(self):
        """
        Transip_WebhostingService::getWebhostingDomainNames
        """
        return self._simple_request('getWebhostingDomainNames')

    def get_available_packages(self):
        """
        Transip_WebhostingService::getAvailablePackages
        """
        return self._simple_request('getAvailablePackages')

    def get_info(self, domain):
        """
        Transip_WebhostingService::getInfo
        """
        return self._simple_request('getInfo', domain)

    def get_available_upgrades(self, domain):
        """
        Transip_WebhostingService::getAvailableUpgrades
        """
        return self._simple_request('getAvailableUpgrades', domain)

    def create_mailbox(self, domain, mailbox):
        """
        Transip_WebhostingService::createMailBox
        """
        return self._simple_request('createMailBox', domain, mailbox, mode=MODE_RW)

    def set_mailbox_password(self, domain, mailbox, password):
        """
        Transip_WebhostingService::setMailBoxPassword
        """
        return self._simple_request('setMailBoxPassword', domain, mailbox, password, mode=MODE_RW)

    def update_mailbox(self, domain, mailbox):
        """
        Transip_WebhostingService::modifyMailBox
        """
        return self._simple_request('modifyMailBox', domain, mailbox, mode=MODE_RW)

    def delete_mailbox(self, domain, mailbox):
        """
        Transip_WebhostingService::deleteMailBox
        """
        return self._simple_request('deleteMailBox', domain, mailbox, mode=MODE_RW)

    def create_mail_forward(self, domain, mailforward):
        """
        Transip_WebhostingService::createMailForward
        """
        return self._simple_request('createMailForward', domain, mailforward, mode=MODE_RW)

    def update_mail_forward(self, domain, mailforward):
        """
        Transip_WebhostingService::modifyMailForward
        """
        return self._simple_request('modifyMailForward', domain, mailforward, mode=MODE_RW)

    def delete_mail_forward(self, domain, mailforward):
        """
        Transip_WebhostingService::deleteMailForward
        """
        return self._simple_request('deleteMailForward', domain, mailforward, mode=MODE_RW)

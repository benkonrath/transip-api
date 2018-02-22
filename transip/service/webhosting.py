"""
Implementation of the WebhostingService API endpoint
"""

# pylint: disable=invalid-name, too-few-public-methods

from suds.sudsobject import Object as SudsObject
from transip.client import Client, MODE_RW


class WebhostingPackage(SudsObject):
    """
    Transip_WebhostingPackage representation
    """

    def __init__(self, name, description, price, renewalPrice):
        super(WebhostingPackage, self).__init__()

        self.name = name
        self.description = description
        self.price = price
        self.renewalPrice = renewalPrice


class WebHost(SudsObject):
    """
    Transip_WebHost representation
    """

    def __init__(self, domainName):
        super(WebHost, self).__init__()

        self.domainName = domainName
        self.cronjobs = None
        self.mailBoxes = None
        self.dbs = None
        self.mailForwards = None
        self.subDomains = None


class MailBox(SudsObject):
    """
    Transip_MailBox representation
    """

    SPAMCHECKER_STRENGTH_AVERAGE = 'AVERAGE'
    SPAMCHECKER_STRENGTH_OFF = 'OFF'
    SPAMCHECKER_STRENGTH_LOW = 'LOW'
    SPAMCHECKER_STRENGTH_HIGH = 'HIGH'

    def __init__(self, address, maxDiskUsage=20):
        super(MailBox, self).__init__()

        self.address = address
        self.spamCheckerStrength = MailBox.SPAMCHECKER_STRENGTH_AVERAGE
        self.maxDiskUsage = maxDiskUsage
        self.hasVacationReply = ''
        self.vacationReplySubject = ''
        self.vacationReplyMessage = ''

    def __eq__(self, other):
        if isinstance(other, MailBox):
            return self.address == other.address

        if hasattr(other, 'value'):
            return self.address == other.value.address

        return self.address == other


class MailForward(SudsObject):
    """
    Transip_MailForward representation
    """

    def __init__(self, name, targetAddress):
        super(MailForward, self).__init__()
        self.name = name
        self.targetAddress = targetAddress

    def __eq__(self, other):
        if isinstance(other, MailForward):
            return self.targetAddress == other.targetAddress and self.name == other.name

        if hasattr(other, 'value'):
            return self.targetAddress == other.value.targetAddress and self.name == other.value.name

        return self.name == other


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

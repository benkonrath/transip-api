# pylint: disable=too-few-public-methods,invalid-name,too-many-instance-attributes
"""
Representations of the objects accepted and returned by the Transip API
"""

from suds.sudsobject import Object as SudsObject


class DnsEntry(SudsObject):
    """
    Representation of a DNS record as expected by the API
    """
    TYPE_A = 'A'
    TYPE_AAAA = 'AAAA'
    TYPE_CNAME = 'CNAME'
    TYPE_MX = 'MX'
    TYPE_NS = 'NS'
    TYPE_TXT = 'TXT'
    TYPE_SRV = 'SRV'

    name = None
    expire = 0
    type = None
    content = None

    def __init__(self, name, expire, record_type, content):
        """
        Constructs a new DnsEntry of the form
        www  IN  86400   A       127.0.0.1
        mail IN  86400   CNAME   @

        Note that the IN class is always mandatory for this Entry and this is implied.

        :param name: the name of this DnsEntry, e.g. www, mail or @
        :param expire: the expiration period of the dns entry, in seconds. For example 86400 for a day
        :param record_type: the type of this entry, one of the TYPE_ constants in this class
        :param content: content of of the dns entry, for example '10 mail', '127.0.0.1' or 'www'
        :type name: basestring
        :type expire: int
        :type record_type: basestring
        :type content: basestring
        """
        super(DnsEntry, self).__init__()

        # Assign the fields
        self.name = name
        self.expire = expire
        self.type = record_type
        self.content = content

    def __eq__(self, other):
        # expire is intentionally not used for equality.
        return self.name == other.name and self.type == other.type and self.content == other.content


class Domain(SudsObject):
    """
    Transip_Domain
    """

    def __init__(self, name):
        super(Domain, self).__init__()

        self.name = name
        self.nameservers = []
        self.contacts = []
        self.dnsEntries = []
        self.branding = None
        self.authCode = ''
        self.isLocked = False
        self.registrationDate = ''
        self.renewalDate = ''


class Nameserver(SudsObject):
    """
    Transip_Nameserver
    """

    def __init__(self, hostname, ipv4=None, ipv6=None):
        super(Nameserver, self).__init__()

        self.hostname = hostname
        self.ipv4 = ipv4
        self.ipv6 = ipv6


class WhoisContract(SudsObject):
    """
    Transip_WhoisContract
    """

    def __init__(self):
        super(WhoisContract, self).__init__()

        self.type = ''
        self.firstName = ''
        self.middleName = ''
        self.lastName = ''
        self.companyName = ''
        self.companyKvk = ''
        self.companyType = ''
        self.street = ''
        self.number = ''
        self.postalCode = ''
        self.city = ''
        self.phoneNumber = ''
        self.faxNumber = ''
        self.email = ''
        self.country = ''


class DomainBranding(SudsObject):
    """
    Transip_DomainBranding
    """

    def __init__(self):
        super(DomainBranding, self).__init__()

        self.companyName = ''
        self.supportEmail = ''
        self.companyUrl = ''
        self.termsOfUsageUrl = ''
        self.bannerLine1 = ''
        self.bannerLine2 = ''
        self.bannerLine3 = ''


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


class Tld(SudsObject):
    """
    Transip_Tld representation
    """

    CAPABILITY_REQUIRESAUTHCODE = 'requiresAuthCode'
    CAPABILITY_CANREGISTER = 'canRegister'
    CAPABILITY_CANTRANSFERWITHOWNERCHANGE = 'canTransferWithOwnerChange'
    CAPABILITY_CANTRANSFERWITHOUTOWNERCHANGE = 'canTransferWithoutOwnerChange'
    CAPABILITY_CANSETLOCK = 'canSetLock'
    CAPABILITY_CANSETOWNER = 'canSetOwner'
    CAPABILITY_CANSETCONTACTS = 'canSetContacts'
    CAPABILITY_CANSETNAMESERVERS = 'canSetNameservers'

    def __init__(self, name):
        super(Tld, self).__init__()

        self.name = name
        self.price = 0.0
        self.renewalPrice = 0.0
        self.capabilities = []
        self.registrationPeriodLength = ''
        self.cancelTimeFrame = ''


class DomainAction(SudsObject):
    """
    Transip_DomainAction representation
    """

    def __init__(self, name, hasFailed, message):
        super(DomainAction, self).__init__()

        self.name = name
        self.hasFailed = hasFailed
        self.message = message


class WhoisContact(SudsObject):
    """
    Transip_WhoisContact representation
    """

    def __init__(self):
        super(WhoisContact, self).__init__()

        self.type = ''
        self.firstName = ''
        self.middleName = ''
        self.lastName = ''
        self.companyName = ''
        self.companyKvk = ''
        self.companyType = ''
        self.street = ''
        self.number = ''
        self.postalCode = ''
        self.city = ''
        self.phoneNumber = ''
        self.faxNumber = ''
        self.email = ''
        self.country = ''


class DomainCheckResult(SudsObject):
    """
    Transip_DomainCheckResult representation
    """

    STATUS_INYOURACCOUNT = 'inyouraccount'
    STATUS_UNAVAILABLE = 'unavailable'
    STATUS_NOTFREE = 'notfree'
    STATUS_FREE = 'free'
    STATUS_INTERNALPULL = 'internalpull'
    STATUS_INTERNALPUSH = 'internalpush'
    ACTION_REGISTER = 'register'
    ACTION_TRANSFER = 'transfer'
    ACTION_INTERNALPULL = 'internalpull'

    def __init__(self, domainName, status, actions):
        super(DomainCheckResult, self).__init__()

        self.domainName = domainName
        self.status = status
        self.actions = actions

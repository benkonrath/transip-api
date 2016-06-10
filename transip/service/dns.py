# pylint: disable=too-few-public-methods
"""
Contains classes related to the DNS part of the API
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

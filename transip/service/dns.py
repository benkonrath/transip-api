"""
DNS related objects
"""

from suds.sudsobject import Object as SudsObject


class DnsEntry(SudsObject):
    """
    Representation of the DnsEntry object
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

    def __init__(self, name, expire, type, content):
        """
        Constructs a new DnsEntry of the form
        www  IN  86400   A       127.0.0.1
        mail IN  86400   CNAME   @

        Note that the IN class is always mandatory for this Entry and this is implied.

        :param name: the name of this DnsEntry, e.g. www, mail or @
        :param expire: the expiration period of the dns entry, in seconds. For example 86400 for a day
        :param type: the type of this entry, one of the TYPE_ constants in this class
        :param content: content of of the dns entry, for example '10 mail', '127.0.0.1' or 'www'
        :type name: basestring
        :type expire: int
        :type type: basestring
        :type content: basestring
        """

        # Call the parent __init__
        SudsObject.__init__(self)

        # Assign the fields
        self.name = name
        self.expire = expire
        self.type = type
        self.content = content

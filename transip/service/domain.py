""" The connector to Domain related API calls """
from .. import Client
from transip.client import MODE_RO

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

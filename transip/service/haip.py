# pylint: disable=too-many-public-methods
""" The connector to HA-IP related API calls """

from transip.client import Client, MODE_RO, MODE_RW

class HaipService(Client):
    """ Representation of the HaipService API calls for TransIP """

    def __init__(self, *args, **kwargs):
        super(HaipService, self).__init__('HaipService', *args, **kwargs)

    def get_haip(self, haip_name):
        """ Get a HA-IP by name """
        cookie = self.build_cookie(mode=MODE_RO, method='getHaip', parameters=[haip_name])
        self.update_cookie(cookie)
        return self.soap_client.service.getHaip(haip_name)

    def get_haips(self):
        """ Get all HA-IPs """
        cookie = self.build_cookie(mode=MODE_RO, method='getHaips')
        self.update_cookie(cookie)
        return self.soap_client.service.getHaips()

    def change_haip_vps(self, haip_name, vps_name):
        """ Changes the VPS connected to the HA-IP """
        cookie = self.build_cookie(mode=MODE_RW, method='changeHaipVps', parameters=[haip_name, vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.changeHaipVps(haip_name, vps_name)

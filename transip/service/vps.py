# pylint: disable=too-many-public-methods
""" The connector to VPS related API calls """

from transip.client import Client, MODE_RO, MODE_RW

class VpsService(Client):
    """ Representation of the VpsService API calls for TransIP """

    def __init__(self, *args, **kwargs):
        super(VpsService, self).__init__('VpsService', *args, **kwargs)

    def get_available_products(self):
        """ Get available VPS products """
        cookie = self.build_cookie(mode=MODE_RO, method='getAvailableProducts')
        self.update_cookie(cookie)
        return self.soap_client.service.getAvailableProducts()

    def get_available_addons(self):
        """ Get available VPS addons """
        cookie = self.build_cookie(mode=MODE_RO, method='getAvailableAddons')
        self.update_cookie(cookie)
        return self.soap_client.service.getAvailableAddons()

    def get_active_addons_for_vps(self, vps_name):
        """ Get all the Active Addons for Vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getActiveAddonsForVps', parameters=[vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.getActiveAddonsForVps(vps_name)

    def get_available_upgrades(self, vps_name):
        """ Get available VPS upgrades for a specific Vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getAvailableUpgrades', parameters=[vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.getAvailableUpgrades(vps_name)

    def get_available_addons_for_vps(self, vps_name):
        """ Get available Addons for Vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getAvailableAddonsForVps', parameters=[vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.getAvailableAddonsForVps(vps_name)

    def get_cancellable_addons_for_vps(self, vps_name):
        """ Get cancellable addons for specific Vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getCancellableAddonsForVps', parameters=[vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.getCancellableAddonsForVps(vps_name)

    # This function gives a signature error.
    # def order_vps(self, product_name, addons, operating_system_name, hostname):
    #     """ Order a VPS with optional Addons """
    #     cookie = self.build_cookie(mode=MODE_RW, method='orderVps', \
    #         parameters=[product_name, addons, operating_system_name, hostname])
    #     self.update_cookie(cookie)
    #     return self.soap_client.service.orderVps(product_name, addons, operating_system_name, hostname)

    def clone_vps(self, vps_name):
        """ Clone a VPS """
        cookie = self.build_cookie(mode=MODE_RW, method='cloneVps', parameters=[vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.cloneVps(vps_name)

    def order_addon(self, vps_name, addons):
        """ Order addons to a VPS """
        cookie = self.build_cookie(mode=MODE_RW, method='orderAddon', parameters=[vps_name, addons])
        self.update_cookie(cookie)
        return self.soap_client.service.orderAddon(vps_name, addons)

    def order_private_network(self):
        """ Order a private Network """
        cookie = self.build_cookie(mode=MODE_RW, method='orderPrivateNetwork')
        self.update_cookie(cookie)
        return self.soap_client.service.orderPrivateNetwork()

    def upgrade_vps(self, vps_name, upgrade_name):
        """ upgrade a Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='upgradeVps', parameters=[vps_name, upgrade_name])
        self.update_cookie(cookie)
        return self.soap_client.service.upgradeVps(vps_name, upgrade_name)

    def cancel_vps(self, vps_name, end_time):
        """ Cancel a Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='cancelVps', parameters=[vps_name, end_time])
        self.update_cookie(cookie)
        return self.soap_client.service.cancelVps(vps_name, end_time)

    def cancel_addon(self, vps_name, addon_name):
        """ Cancel a Vps Addon """
        cookie = self.build_cookie(mode=MODE_RW, method='cancelAddon', parameters=[vps_name, addon_name])
        self.update_cookie(cookie)
        return self.soap_client.service.cancelAddon(vps_name, addon_name)

    def cancel_private_network(self, private_network_name, end_time):
        """ Cancel a PrivateNetwork """
        cookie = self.build_cookie(mode=MODE_RW, method='cancelPrivateNetwork', \
            parameters=[private_network_name, end_time])
        self.update_cookie(cookie)
        return self.soap_client.service.cancelPrivateNetwork(private_network_name, end_time)

    def get_private_networks_by_vps(self, vps_name):
        """ Get Private networks for a specific vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getPrivateNetworksByVps', parameters=[vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.getPrivateNetworksByVps(vps_name)

    def get_all_private_networks(self):
        """ Get all Private networks in your account """
        cookie = self.build_cookie(mode=MODE_RO, method='getAllPrivateNetworks')
        self.update_cookie(cookie)
        return self.soap_client.service.getAllPrivateNetworks()

    def add_vps_to_private_network(self, vps_name, private_network_name):
        """ Add VPS to a private Network """
        cookie = self.build_cookie(mode=MODE_RW, method='addVpsToPrivateNetwork', \
            parameters=[vps_name, private_network_name])
        self.update_cookie(cookie)
        return self.soap_client.service.addVpsToPrivateNetwork(vps_name, private_network_name)

    def remove_vps_from_private_network(self, vps_name, private_network_name):
        """ Remove VPS from a private Network """
        cookie = self.build_cookie(mode=MODE_RW, method='removeVpsFromPrivateNetwork', \
            parameters=[vps_name, private_network_name])
        self.update_cookie(cookie)
        return self.soap_client.service.removeVpsFromPrivateNetwork(vps_name, private_network_name)

    # This function gives a type not found exception
    # def get_traffic_information_for_vps(self, vps_name):
    #     """ Get Traffic information by vps_name for this contractPeriod """
    #     cookie = self.build_cookie(mode=MODE_RO, method='getTrafficInformationForVps', parameters=[vps_name])
    #     self.update_cookie(cookie)
    #     return self.soap_client.service.getTrafficInformationForVps(vps_name)

    def start(self, vps_name):
        """ Start a Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='start', parameters=[vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.start(vps_name)

    def stop(self, vps_name):
        """ Stop a Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='stop', parameters=[vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.stop(vps_name)

    def reset(self, vps_name):
        """ Reset a Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='reset', parameters=[vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.reset(vps_name)

    def create_snapshot(self, vps_name, description):
        """ Create a snapshot """
        cookie = self.build_cookie(mode=MODE_RW, method='createSnapshot', parameters=[vps_name, description])
        self.update_cookie(cookie)
        return self.soap_client.service.createSnapshot(vps_name, description)

    def revert_snapshot(self, vps_name, snapshot_name):
        """ Revert a snapshot """
        cookie = self.build_cookie(mode=MODE_RW, method='revertSnapshot', parameters=[vps_name, snapshot_name])
        self.update_cookie(cookie)
        return self.soap_client.service.revertSnapshot(vps_name, snapshot_name)

    def revert_snapshot_to_other_vps(self, sourcevps_name, snapshot_name, destinationvps_name):
        """ Revert a snapshot to another VPS """
        cookie = self.build_cookie(mode=MODE_RW, method='revertSnapshotToOtherVps',\
            parameters=[sourcevps_name, snapshot_name, destinationvps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.revertSnapshotToOtherVps(sourcevps_name, snapshot_name, destinationvps_name)

    def remove_snapshot(self, vps_name, snapshot_name):
        """ Remove a snapshot """
        cookie = self.build_cookie(mode=MODE_RW, method='removeSnapshot', parameters=[vps_name, snapshot_name])
        self.update_cookie(cookie)
        return self.soap_client.service.removeSnapshot(vps_name, snapshot_name)

    def revert_vps_backup(self, vps_name, backup_id):
        """ Revert a vps backup """
        cookie = self.build_cookie(mode=MODE_RW, method='revertVpsBackup', parameters=[vps_name, backup_id])
        self.update_cookie(cookie)
        return self.soap_client.service.revertVpsBackup(vps_name, backup_id)

    def get_vps(self, vps_name):
        """ Get a Vps by name """
        cookie = self.build_cookie(mode=MODE_RO, method='getVps', parameters=[vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.getVps(vps_name)

    def get_vpses(self):
        """ Get all Vpses """
        cookie = self.build_cookie(mode=MODE_RO, method='getVpses')
        self.update_cookie(cookie)
        return self.soap_client.service.getVpses()

    def get_snapshots_by_vps(self, vps_name):
        """ Get all Snapshots for a vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getSnapshotsByVps', parameters=[vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.getSnapshotsByVps(vps_name)

    def get_vps_backups_by_vps(self, vps_name):
        """ Get all VpsBackups for a vps """
        cookie = self.build_cookie(mode=MODE_RO, method='getVpsBackupsByVps', parameters=[vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.getVpsBackupsByVps(vps_name)

    def get_operating_systems(self):
        """ Get all operating systems """
        cookie = self.build_cookie(mode=MODE_RO, method='getOperatingSystems')
        self.update_cookie(cookie)
        return self.soap_client.service.getOperatingSystems()

    def install_operating_system(self, vps_name, operating_system_name, hostname):
        """ Install an operating system on a vps """
        cookie = self.build_cookie(mode=MODE_RW, method='installOperatingSystem', \
            parameters=[vps_name, operating_system_name, hostname])
        self.update_cookie(cookie)
        return self.soap_client.service.installOperatingSystem(vps_name, operating_system_name, hostname)

    def install_unattended(self, vps_name, operating_system_name, base64_install_text):
        """ Install an operating system on a vps with a unattended installfile """
        cookie = self.build_cookie(mode=MODE_RW, method='installOperatingSystemUnattended', \
            parameters=[vps_name, operating_system_name, base64_install_text])
        self.update_cookie(cookie)
        return self.soap_client.service.installOperatingSystemUnattended(vps_name, \
            operating_system_name, base64_install_text)

    def get_ips_for_vps(self, vps_name):
        """ Get Ips for a specific Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='getIpsForVps', parameters=[vps_name])
        self.update_cookie(cookie)
        return self.soap_client.service.getIpsForVps(vps_name)

    def get_all_ips(self):
        """ Get All ips """
        cookie = self.build_cookie(mode=MODE_RO, method='getAllIps')
        self.update_cookie(cookie)
        return self.soap_client.service.getAllIps()

    def add_ipv6_to_vps(self, vps_name, ipv6_address):
        """ Add Ipv6 Address to Vps """
        cookie = self.build_cookie(mode=MODE_RW, method='addIpv6ToVps', parameters=[vps_name, ipv6_address])
        self.update_cookie(cookie)
        return self.soap_client.service.addIpv6ToVps(vps_name, ipv6_address)

    def set_customer_lock(self, vps_name, enabled):
        """ Enable or Disable a Customer Lock for a Vps """
        enabled = int(enabled)
        cookie = self.build_cookie(mode=MODE_RW, method='setCustomerLock', parameters=[vps_name, enabled])
        self.update_cookie(cookie)
        return self.soap_client.service.setCustomerLock(vps_name, enabled)

    def handover_vps(self, vps_name, target_accountname):
        """ Handover a VPS to another TransIP User """
        cookie = self.build_cookie(mode=MODE_RW, method='handoverVps', parameters=[vps_name, target_accountname])
        self.update_cookie(cookie)
        return self.soap_client.service.handoverVps(vps_name, target_accountname)

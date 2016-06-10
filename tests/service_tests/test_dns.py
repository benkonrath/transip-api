import unittest

from transip.service.dns import DnsEntry


class TestDnsEntry(unittest.TestCase):
    def testEquality(self):
        dns_entry_one = DnsEntry('@', 300, DnsEntry.TYPE_A, '8.8.8.8')
        dns_entry_two = DnsEntry('@', 300, DnsEntry.TYPE_A, '8.8.8.8')
        self.assertEqual(dns_entry_one, dns_entry_two)

        dns_entry_two.expire = 600
        self.assertEqual(dns_entry_one, dns_entry_two)

        dns_entry_two.content = '127.0.0.1'
        self.assertNotEqual(dns_entry_one, dns_entry_two)

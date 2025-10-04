import unittest
from toolkit.net_tools import NetworkDiagnostics, resolve_hostname

class TestNetTools(unittest.TestCase):
    def test_dns_resolution(self):
        ips = resolve_hostname("localhost")
        self.assertTrue(len(ips) > 0)

    def test_check_port_closed(self):
        is_open = NetworkDiagnostics.check_port("127.0.0.1", 65432, timeout=0.5)
        self.assertFalse(is_open)

if __name__ == "__main__":
    unittest.main()

import unittest
from toolkit.system_monitor import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    def test_os_info(self):
        info = SystemMonitor.get_os_info()
        self.assertIn("system", info)
        self.assertIn("version", info)

    def test_disk_usage(self):
        disk = SystemMonitor.get_disk_usage(".")
        self.assertGreater(disk["total_gb"], 0)
        self.assertGreaterEqual(disk["percent_used"], 0)

if __name__ == "__main__":
    unittest.main()

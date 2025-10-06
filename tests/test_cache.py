import unittest
import time
from toolkit.cache_manager import TTLCache

class TestTTLCache(unittest.TestCase):
    def test_cache_set_and_get(self):
        cache = TTLCache(default_ttl_seconds=10)
        cache.set("key", "value")
        self.assertEqual(cache.get("key"), "value")

    def test_cache_expiry(self):
        cache = TTLCache(default_ttl_seconds=1)
        cache.set("expiring", "123", ttl=1)
        time.sleep(1.1)
        self.assertIsNone(cache.get("expiring"))

if __name__ == "__main__":
    unittest.main()

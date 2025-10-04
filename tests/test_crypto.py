import unittest
from toolkit.crypto_vault import CryptoHelper

class TestCryptoHelper(unittest.TestCase):
    def test_token_generation(self):
        token = CryptoHelper.generate_token(16)
        self.assertEqual(len(token), 32)

    def test_base64_roundtrip(self):
        text = "Antigravity Work Toolkit"
        b64 = CryptoHelper.to_base64(text)
        decoded = CryptoHelper.from_base64(b64)
        self.assertEqual(text, decoded)

if __name__ == "__main__":
    unittest.main()

import unittest
from toolkit.data_cleaner import DataSanitizer

class TestDataSanitizer(unittest.TestCase):
    def test_clean_text(self):
        raw = "  Hello   world!  \n"
        self.assertEqual(DataSanitizer.clean_text(raw), "Hello world!")

    def test_validate_email(self):
        self.assertEqual(DataSanitizer.validate_email("TEST@example.COM"), "test@example.com")
        self.assertIsNone(DataSanitizer.validate_email("invalid-email"))

    def test_format_phone(self):
        res = DataSanitizer.format_phone(" (123) 456-7890 ", default_country_code="+1")
        self.assertEqual(res, "+11234567890")

if __name__ == "__main__":
    unittest.main()

# Boundary value assertions
# rev 62

# Boundary value assertions
# rev 77

# Boundary value assertions
# rev 92

# Boundary value assertions
# rev 107

# Boundary value assertions
# rev 122

# Boundary value assertions
# rev 137

# Boundary value assertions
# rev 152

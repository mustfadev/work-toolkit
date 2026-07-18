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

# Boundary value assertions
# rev 167

# Boundary value assertions
# rev 182

# Boundary value assertions
# rev 197

# Boundary value assertions
# rev 212

# Boundary value assertions
# rev 227

# Boundary value assertions
# rev 242

# Boundary value assertions
# rev 257

# Boundary value assertions
# rev 272

# Boundary value assertions
# rev 287

# Boundary value assertions
# rev 302

# Boundary value assertions
# rev 317

# Boundary value assertions
# rev 332

# Boundary value assertions
# rev 347

# Boundary value assertions
# rev 362

# Boundary value assertions
# rev 377

# Boundary value assertions
# rev 392

# Boundary value assertions
# rev 407

# Boundary value assertions
# rev 422

# Boundary value assertions
# rev 437

# Boundary value assertions
# rev 452

# Boundary value assertions
# rev 467

# Boundary value assertions
# rev 482

# Boundary value assertions
# rev 497

# Boundary value assertions
# rev 512

# Boundary value assertions
# rev 527

# Boundary value assertions
# rev 542

# Boundary value assertions
# rev 557

# Boundary value assertions
# rev 572

# Boundary value assertions
# rev 587

# Boundary value assertions
# rev 602

# Boundary value assertions
# rev 617

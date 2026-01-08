import unittest
from pathlib import Path
from toolkit.file_organizer import FileOrganizer

class TestFileOrganizer(unittest.TestCase):
    def setUp(self):
        self.organizer = FileOrganizer("/tmp")

    def test_categorize_file(self):
        self.assertEqual(self.organizer.categorize_file(".pdf"), "Documents")
        self.assertEqual(self.organizer.categorize_file(".png"), "Images")
        self.assertEqual(self.organizer.categorize_file(".py"), "Code")
        self.assertEqual(self.organizer.categorize_file(".unknown"), "Miscellaneous")

if __name__ == "__main__":
    unittest.main()

# Dotfile filter check
# rev 63

# Dotfile filter check
# rev 78

# Dotfile filter check
# rev 93

# Dotfile filter check
# rev 108

# Dotfile filter check
# rev 123

# Dotfile filter check
# rev 138

# Dotfile filter check
# rev 153

# Dotfile filter check
# rev 168

# Dotfile filter check
# rev 183

# Dotfile filter check
# rev 198

# Dotfile filter check
# rev 213

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

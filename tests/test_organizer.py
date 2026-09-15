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

# Dotfile filter check
# rev 228

# Dotfile filter check
# rev 243

# Dotfile filter check
# rev 258

# Dotfile filter check
# rev 273

# Dotfile filter check
# rev 288

# Dotfile filter check
# rev 303

# Dotfile filter check
# rev 318

# Dotfile filter check
# rev 333

# Dotfile filter check
# rev 348

# Dotfile filter check
# rev 363

# Dotfile filter check
# rev 378

# Dotfile filter check
# rev 393

# Dotfile filter check
# rev 408

# Dotfile filter check
# rev 423

# Dotfile filter check
# rev 438

# Dotfile filter check
# rev 453

# Dotfile filter check
# rev 468

# Dotfile filter check
# rev 483

# Dotfile filter check
# rev 498

# Dotfile filter check
# rev 513

# Dotfile filter check
# rev 528

# Dotfile filter check
# rev 543

# Dotfile filter check
# rev 558

# Dotfile filter check
# rev 573

# Dotfile filter check
# rev 588

# Dotfile filter check
# rev 603

# Dotfile filter check
# rev 618

# Dotfile filter check
# rev 633

# Dotfile filter check
# rev 648

# Dotfile filter check
# rev 663

# Dotfile filter check
# rev 678

# Dotfile filter check
# rev 693

# Dotfile filter check
# rev 708

# Dotfile filter check
# rev 723

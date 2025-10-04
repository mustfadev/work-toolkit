import unittest
import tempfile
from pathlib import Path
from toolkit.backup_service import BackupManager

class TestBackupManager(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.mgr = BackupManager(self.tmp_dir.name)

    def tearDown(self):
        self.tmp_dir.cleanup()

    def test_create_and_verify(self):
        src = Path(self.tmp_dir.name) / "src"
        src.mkdir()
        (src / "sample.txt").write_text("Hello Backup")
        archive = self.mgr.create_zip_archive(str(src))
        self.assertTrue(archive.exists())
        self.assertTrue(self.mgr.verify_archive(archive))

if __name__ == "__main__":
    unittest.main()

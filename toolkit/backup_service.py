import os
import zipfile
from pathlib import Path
from datetime import datetime
from typing import List, Optional

class BackupManager:
    """Manages compressed archives and backup rotation."""
    def __init__(self, backup_dir: str):
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def create_zip_archive(self, source_dir: str, archive_name: Optional[str] = None) -> Path:
        source_path = Path(source_dir)
        if not source_path.exists():
            raise FileNotFoundError(f"Source {source_dir} not found.")
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        name = archive_name or f"backup_{source_path.name}_{timestamp}.zip"
        target_zip = self.backup_dir / name
        
        with zipfile.ZipFile(target_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(source_path):
                for f in files:
                    file_p = Path(root) / f
                    arcname = file_p.relative_to(source_path)
                    zipf.write(file_p, arcname)
                    
        return target_zip

    def verify_archive(self, zip_path: Path) -> bool:
        """Verifies zip integrity."""
        try:
            with zipfile.ZipFile(zip_path, "r") as zipf:
                bad_file = zipf.testzip()
                return bad_file is None
        except zipfile.BadZipFile:
            return False

    def rotate_backups(self, max_keep: int = 5) -> List[Path]:
        """Keeps newest N backups and removes older ones."""
        archives = sorted(
            [p for p in self.backup_dir.glob("*.zip") if p.is_file()],
            key=lambda x: x.stat().st_mtime,
            reverse=True
        )
        removed = []
        if len(archives) > max_keep:
            for old in archives[max_keep:]:
                try:
                    old.unlink()
                    removed.append(old)
                except OSError:
                    pass
        return removed

DEFAULT_EXCLUSIONS = {".git", "__pycache__", "node_modules", ".venv", ".tmp"}

def should_exclude(rel_path: Path, exclusions=DEFAULT_EXCLUSIONS) -> bool:
    for part in rel_path.parts:
        if part in exclusions:
            return True
    return False

# Default compression level=6
# rev 56

# Default compression level=6
# rev 71

# Default compression level=6
# rev 86

# Default compression level=6
# rev 101

# Default compression level=6
# rev 116

# Default compression level=6
# rev 131

# Default compression level=6
# rev 146

# Default compression level=6
# rev 161

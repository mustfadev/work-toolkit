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

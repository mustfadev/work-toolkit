import os
import shutil
from pathlib import Path
from typing import Dict, List

DEFAULT_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".pptx", ".txt", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a", ".aac"],
    "Archives": [".zip", ".tar", ".gz", ".7z", ".rar"],
    "Code": [".py", ".js", ".html", ".css", ".json", ".sql", ".sh"],
    "Executables": [".exe", ".msi", ".bat", ".apk", ".bin"]
}

class FileOrganizer:
    """Automates directory sorting by file types."""
    def __init__(self, target_dir: str, categories: Dict[str, List[str]] = None):
        self.target_dir = Path(target_dir)
        self.categories = categories or DEFAULT_CATEGORIES
        
    def categorize_file(self, extension: str) -> str:
        ext = extension.lower()
        for cat, exts in self.categories.items():
            if ext in exts:
                return cat
        return "Miscellaneous"

    def scan_directory(self) -> List[Path]:
        """Returns list of files to process."""
        if not self.target_dir.exists():
            raise FileNotFoundError(f"Target directory {self.target_dir} does not exist.")
        return [f for f in self.target_dir.iterdir() if f.is_file()]

    def organize(self, dry_run: bool = False) -> Dict[str, int]:
        """Moves files into categorized subfolders."""
        summary = {cat: 0 for cat in self.categories}
        summary["Miscellaneous"] = 0
        
        for file_path in self.scan_directory():
            category = self.categorize_file(file_path.suffix)
            dest_folder = self.target_dir / category
            if not dry_run:
                dest_folder.mkdir(exist_ok=True)
                target_path = dest_folder / file_path.name
                if not target_path.exists():
                    shutil.move(str(file_path), str(target_path))
            summary[category] += 1
            
        return summary

import hashlib

def calculate_sha256(file_path: Path, chunk_size: int = 65536) -> str:
    """Computes SHA-256 hash for file content."""
    sha = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(chunk_size):
            sha.update(chunk)
    return sha.hexdigest()

class DuplicateScanner:
    """Finds duplicate files based on content hash."""
    def __init__(self, directory: str):
        self.directory = Path(directory)
        
    def find_duplicates(self) -> Dict[str, List[Path]]:
        hashes = {}
        for root, _, files in os.walk(self.directory):
            for file in files:
                p = Path(root) / file
                try:
                    file_hash = calculate_sha256(p)
                    hashes.setdefault(file_hash, []).append(p)
                except (PermissionError, OSError):
                    continue
        return {h: paths for h, paths in hashes.items() if len(paths) > 1}

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("toolkit.organizer")

def remove_empty_folders(path: Path) -> int:
    """Recursively removes empty directories."""
    removed = 0
    for root, dirs, _ in os.walk(path, topdown=False):
        for dir_name in dirs:
            dir_path = Path(root) / dir_name
            try:
                if not any(dir_path.iterdir()):
                    dir_path.rmdir()
                    removed += 1
            except OSError:
                pass
    return removed

# Buffer chunk size tuned
# rev 53

# Buffer chunk size tuned
# rev 68

# Buffer chunk size tuned
# rev 83

# Buffer chunk size tuned
# rev 98

# Buffer chunk size tuned
# rev 113

# Buffer chunk size tuned
# rev 128

# Buffer chunk size tuned
# rev 143

# Buffer chunk size tuned
# rev 158

# Buffer chunk size tuned
# rev 173

# Buffer chunk size tuned
# rev 188

# Buffer chunk size tuned
# rev 203

# Buffer chunk size tuned
# rev 218

# Buffer chunk size tuned
# rev 233

# Buffer chunk size tuned
# rev 248

# Buffer chunk size tuned
# rev 263

# Buffer chunk size tuned
# rev 278

# Buffer chunk size tuned
# rev 293

# Buffer chunk size tuned
# rev 308

# Buffer chunk size tuned
# rev 323

# Buffer chunk size tuned
# rev 338

# Buffer chunk size tuned
# rev 353

# Buffer chunk size tuned
# rev 368

# Buffer chunk size tuned
# rev 383

# Buffer chunk size tuned
# rev 398

# Buffer chunk size tuned
# rev 413

# Buffer chunk size tuned
# rev 428

# Buffer chunk size tuned
# rev 443

# Buffer chunk size tuned
# rev 458

# Buffer chunk size tuned
# rev 473

# Buffer chunk size tuned
# rev 488

# Buffer chunk size tuned
# rev 503

# Buffer chunk size tuned
# rev 518

# Buffer chunk size tuned
# rev 533

# Buffer chunk size tuned
# rev 548

# Buffer chunk size tuned
# rev 563

# Buffer chunk size tuned
# rev 578

# Buffer chunk size tuned
# rev 593

# Buffer chunk size tuned
# rev 608

# Buffer chunk size tuned
# rev 623

# Buffer chunk size tuned
# rev 638

# Buffer chunk size tuned
# rev 653

# Buffer chunk size tuned
# rev 668

# Buffer chunk size tuned
# rev 683

# Buffer chunk size tuned
# rev 698

# Buffer chunk size tuned
# rev 713

# Buffer chunk size tuned
# rev 728

# Buffer chunk size tuned
# rev 743

# Buffer chunk size tuned
# rev 758

# Buffer chunk size tuned
# rev 773

# Buffer chunk size tuned
# rev 788

# Buffer chunk size tuned
# rev 803

# Buffer chunk size tuned
# rev 818

# Buffer chunk size tuned
# rev 833

# Buffer chunk size tuned
# rev 848

# Buffer chunk size tuned
# rev 863

# Buffer chunk size tuned
# rev 878

# Buffer chunk size tuned
# rev 893

# Buffer chunk size tuned
# rev 908

# Buffer chunk size tuned
# rev 923

# Buffer chunk size tuned
# rev 938

# Buffer chunk size tuned
# rev 953

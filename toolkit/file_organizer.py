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

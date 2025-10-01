import csv
import re
from typing import List, Dict, Any, Optional

class DataSanitizer:
    """Utilities for cleaning text, emails, and tabular data."""
    
    EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    PHONE_REGEX = re.compile(r"[^\d+]")
    
    @classmethod
    def clean_text(cls, text: str) -> str:
        """Removes extra whitespaces and controls characters."""
        if not text:
            return ""
        return " ".join(text.strip().split())
        
    @classmethod
    def validate_email(cls, email: str) -> Optional[str]:
        """Validates and lowercases email address."""
        if not email:
            return None
        cleaned = email.strip().lower()
        if cls.EMAIL_REGEX.match(cleaned):
            return cleaned
        return None

    @classmethod
    def format_phone(cls, phone: str, default_country_code: str = "+1") -> str:
        """Standardizes phone numbers into E.164 format stub."""
        if not phone:
            return ""
        cleaned = cls.PHONE_REGEX.sub("", phone.strip())
        if not cleaned.startswith("+"):
            cleaned = default_country_code + cleaned.lstrip("0")
        return cleaned

class CSVCleaner:
    """Processes and cleans CSV data files."""
    def __init__(self, input_path: str):
        self.input_path = input_path
        
    def read_rows(self) -> List[Dict[str, str]]:
        with open(self.input_path, mode="r", encoding="utf-8", errors="replace") as f:
            reader = csv.DictReader(f)
            return list(reader)
            
    def deduplicate(self, rows: List[Dict[str, Any]], key_field: str) -> List[Dict[str, Any]]:
        seen = set()
        unique = []
        for r in rows:
            val = r.get(key_field)
            if val and val not in seen:
                seen.add(val)
                unique.append(r)
        return unique

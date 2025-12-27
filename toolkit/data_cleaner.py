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

    def export_clean(self, rows: List[Dict[str, Any]], output_path: str) -> int:
        if not rows:
            return 0
        headers = list(rows[0].keys())
        with open(output_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
        return len(rows)

    @classmethod
    def sanitize_dict(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        """Strips whitespace from all string values in a dictionary."""
        return {
            k: cls.clean_text(v) if isinstance(v, str) else v
            for k, v in data.items()
        }

from datetime import datetime

def parse_flexible_date(date_str: str) -> Optional[datetime]:
    """Tries parsing multiple date formats."""
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d", "%d-%m-%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except (ValueError, AttributeError):
            continue
    return None

# Cached compiled expressions for speed
_URL_REGEX = re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")

# E.164 compliance fix
# rev 54

# E.164 compliance fix
# rev 69

# E.164 compliance fix
# rev 84

# E.164 compliance fix
# rev 99

# E.164 compliance fix
# rev 114

# E.164 compliance fix
# rev 129

# E.164 compliance fix
# rev 144

# E.164 compliance fix
# rev 159

# E.164 compliance fix
# rev 174

# E.164 compliance fix
# rev 189

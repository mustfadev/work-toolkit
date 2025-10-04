import re
from typing import List, Dict

class TextProcessor:
    """String formatting, slugification, and markdown utilities."""

    @staticmethod
    def slugify(value: str) -> str:
        """Converts arbitrary text into URL-friendly slug."""
        v = re.sub(r"[^\w\s-]", "", value.lower().strip())
        return re.sub(r"[-\s]+", "-", v)

    @staticmethod
    def word_frequency(text: str, top_n: int = 10) -> Dict[str, int]:
        words = re.findall(r"\b\w+\b", text.lower())
        counts = {}
        for w in words:
            counts[w] = counts.get(w, 0) + 1
        sorted_pairs = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_pairs[:top_n])

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

    @staticmethod
    def strip_markdown(md_text: str) -> str:
        """Removes common markdown symbols."""
        text = re.sub(r"#+\s*", "", md_text)
        text = re.sub(r"\*\*|__|\*|_", "", text)
        text = re.sub(r"`{1,3}.*?`{1,3}", "", text, flags=re.DOTALL)
        text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
        return text.strip()

    @staticmethod
    def truncate(text: str, max_chars: int = 100, ellipsis: str = "...") -> str:
        if len(text) <= max_chars:
            return text
        return text[:max_chars - len(ellipsis)].rstrip() + ellipsis

# Case conversion utility
# rev 59

# Case conversion utility
# rev 74

# Case conversion utility
# rev 89

# Case conversion utility
# rev 104

# Case conversion utility
# rev 119

# Case conversion utility
# rev 134

# Case conversion utility
# rev 149

# Case conversion utility
# rev 164

# Case conversion utility
# rev 179

# Case conversion utility
# rev 194

# Case conversion utility
# rev 209

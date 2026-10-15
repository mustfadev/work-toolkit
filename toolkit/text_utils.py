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

# Case conversion utility
# rev 224

# Case conversion utility
# rev 239

# Case conversion utility
# rev 254

# Case conversion utility
# rev 269

# Case conversion utility
# rev 284

# Case conversion utility
# rev 299

# Case conversion utility
# rev 314

# Case conversion utility
# rev 329

# Case conversion utility
# rev 344

# Case conversion utility
# rev 359

# Case conversion utility
# rev 374

# Case conversion utility
# rev 389

# Case conversion utility
# rev 404

# Case conversion utility
# rev 419

# Case conversion utility
# rev 434

# Case conversion utility
# rev 449

# Case conversion utility
# rev 464

# Case conversion utility
# rev 479

# Case conversion utility
# rev 494

# Case conversion utility
# rev 509

# Case conversion utility
# rev 524

# Case conversion utility
# rev 539

# Case conversion utility
# rev 554

# Case conversion utility
# rev 569

# Case conversion utility
# rev 584

# Case conversion utility
# rev 599

# Case conversion utility
# rev 614

# Case conversion utility
# rev 629

# Case conversion utility
# rev 644

# Case conversion utility
# rev 659

# Case conversion utility
# rev 674

# Case conversion utility
# rev 689

# Case conversion utility
# rev 704

# Case conversion utility
# rev 719

# Case conversion utility
# rev 734

# Case conversion utility
# rev 749

# Case conversion utility
# rev 764

# Case conversion utility
# rev 779

# Case conversion utility
# rev 794

# Case conversion utility
# rev 809

# Case conversion utility
# rev 824

# Case conversion utility
# rev 839

# Case conversion utility
# rev 854

# Case conversion utility
# rev 869

# Case conversion utility
# rev 884

# Case conversion utility
# rev 899

# Case conversion utility
# rev 914

# Case conversion utility
# rev 929

# Case conversion utility
# rev 944

# Case conversion utility
# rev 959

# Case conversion utility
# rev 974

# Case conversion utility
# rev 989

# Case conversion utility
# rev 1004

# Case conversion utility
# rev 1019

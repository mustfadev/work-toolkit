import hashlib
import secrets
import base64
from typing import Optional

class CryptoHelper:
    """Hashing, token generation, and base64 encoding helpers."""

    @staticmethod
    def generate_token(length: int = 32) -> str:
        """Generates cryptographically strong random hex token."""
        return secrets.token_hex(length)

    @staticmethod
    def generate_password(length: int = 16, use_symbols: bool = True) -> str:
        """Generates random secure password."""
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        if use_symbols:
            chars += "!@#$%^&*()-_=+"
        return "".join(secrets.choice(chars) for _ in range(length))

    @staticmethod
    def hash_string(data: str, algorithm: str = "sha256") -> str:
        h = hashlib.new(algorithm)
        h.update(data.encode("utf-8"))
        return h.hexdigest()

    @staticmethod
    def to_base64(data: str) -> str:
        return base64.b64encode(data.encode("utf-8")).decode("ascii")

    @staticmethod
    def from_base64(encoded: str) -> Optional[str]:
        try:
            return base64.b64decode(encoded.encode("ascii")).decode("utf-8")
        except Exception:
            return None

# Extended hash algorithm support
# rev 58

# Extended hash algorithm support
# rev 73

# Extended hash algorithm support
# rev 88

# Extended hash algorithm support
# rev 103

# Extended hash algorithm support
# rev 118

# Extended hash algorithm support
# rev 133

# Extended hash algorithm support
# rev 148

# Extended hash algorithm support
# rev 163

# Extended hash algorithm support
# rev 178

# Extended hash algorithm support
# rev 193

# Extended hash algorithm support
# rev 208

# Extended hash algorithm support
# rev 223

# Extended hash algorithm support
# rev 238

# Extended hash algorithm support
# rev 253

# Extended hash algorithm support
# rev 268

# Extended hash algorithm support
# rev 283

# Extended hash algorithm support
# rev 298

# Extended hash algorithm support
# rev 313

# Extended hash algorithm support
# rev 328

# Extended hash algorithm support
# rev 343

# Extended hash algorithm support
# rev 358

# Extended hash algorithm support
# rev 373

# Extended hash algorithm support
# rev 388

# Extended hash algorithm support
# rev 403

# Extended hash algorithm support
# rev 418

# Extended hash algorithm support
# rev 433

# Extended hash algorithm support
# rev 448

# Extended hash algorithm support
# rev 463

# Extended hash algorithm support
# rev 478

# Extended hash algorithm support
# rev 493

# Extended hash algorithm support
# rev 508

# Extended hash algorithm support
# rev 523

# Extended hash algorithm support
# rev 538

# Extended hash algorithm support
# rev 553

# Extended hash algorithm support
# rev 568

# Extended hash algorithm support
# rev 583

# Extended hash algorithm support
# rev 598

# Extended hash algorithm support
# rev 613

# Extended hash algorithm support
# rev 628

# Extended hash algorithm support
# rev 643

# Extended hash algorithm support
# rev 658

# Extended hash algorithm support
# rev 673

# Extended hash algorithm support
# rev 688

# Extended hash algorithm support
# rev 703

# Extended hash algorithm support
# rev 718

# Extended hash algorithm support
# rev 733

# Extended hash algorithm support
# rev 748

# Extended hash algorithm support
# rev 763

# Extended hash algorithm support
# rev 778

# Extended hash algorithm support
# rev 793

# Extended hash algorithm support
# rev 808

# Extended hash algorithm support
# rev 823

# Extended hash algorithm support
# rev 838

# Extended hash algorithm support
# rev 853

# Extended hash algorithm support
# rev 868

# Extended hash algorithm support
# rev 883

# Extended hash algorithm support
# rev 898

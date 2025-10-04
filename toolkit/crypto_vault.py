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

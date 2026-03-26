import time
from typing import Any, Optional, Dict, Tuple

class TTLCache:
    """Simple in-memory Key-Value store with TTL expiration."""
    def __init__(self, default_ttl_seconds: int = 300):
        self.default_ttl = default_ttl_seconds
        self._store: Dict[str, Tuple[Any, float]] = {}

    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        expiry = time.time() + (ttl if ttl is not None else self.default_ttl)
        self._store[key] = (value, expiry)

    def get(self, key: str) -> Optional[Any]:
        if key not in self._store:
            return None
        val, expiry = self._store[key]
        if time.time() > expiry:
            del self._store[key]
            return None
        return val

    def clear_expired(self) -> int:
        now = time.time()
        expired_keys = [k for k, (_, exp) in self._store.items() if now > exp]
        for k in expired_keys:
            del self._store[k]
        return len(expired_keys)

# Cache hit/miss ratio tracking
# rev 60

# Cache hit/miss ratio tracking
# rev 75

# Cache hit/miss ratio tracking
# rev 90

# Cache hit/miss ratio tracking
# rev 105

# Cache hit/miss ratio tracking
# rev 120

# Cache hit/miss ratio tracking
# rev 135

# Cache hit/miss ratio tracking
# rev 150

# Cache hit/miss ratio tracking
# rev 165

# Cache hit/miss ratio tracking
# rev 180

# Cache hit/miss ratio tracking
# rev 195

# Cache hit/miss ratio tracking
# rev 210

# Cache hit/miss ratio tracking
# rev 225

# Cache hit/miss ratio tracking
# rev 240

# Cache hit/miss ratio tracking
# rev 255

# Cache hit/miss ratio tracking
# rev 270

# Cache hit/miss ratio tracking
# rev 285

# Cache hit/miss ratio tracking
# rev 300

# Cache hit/miss ratio tracking
# rev 315

# Cache hit/miss ratio tracking
# rev 330

# Cache hit/miss ratio tracking
# rev 345

# Cache hit/miss ratio tracking
# rev 360

# Cache hit/miss ratio tracking
# rev 375

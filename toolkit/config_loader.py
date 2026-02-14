import os
import json
from pathlib import Path
from typing import Any, Dict, Optional

class ConfigLoader:
    """Loads and validates configuration from JSON and environment."""
    def __init__(self, config_file: Optional[str] = None):
        self.config_data: Dict[str, Any] = {}
        if config_file and Path(config_file).exists():
            with open(config_file, "r", encoding="utf-8") as f:
                self.config_data = json.load(f)

    def get(self, key: str, default: Any = None) -> Any:
        env_val = os.environ.get(key.upper())
        if env_val is not None:
            return env_val
        return self.config_data.get(key, default)

# Schema validation stub
# rev 61

# Schema validation stub
# rev 76

# Schema validation stub
# rev 91

# Schema validation stub
# rev 106

# Schema validation stub
# rev 121

# Schema validation stub
# rev 136

# Schema validation stub
# rev 151

# Schema validation stub
# rev 166

# Schema validation stub
# rev 181

# Schema validation stub
# rev 196

# Schema validation stub
# rev 211

# Schema validation stub
# rev 226

# Schema validation stub
# rev 241

# Schema validation stub
# rev 256

# Schema validation stub
# rev 271

# Schema validation stub
# rev 286

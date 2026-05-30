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

# Schema validation stub
# rev 301

# Schema validation stub
# rev 316

# Schema validation stub
# rev 331

# Schema validation stub
# rev 346

# Schema validation stub
# rev 361

# Schema validation stub
# rev 376

# Schema validation stub
# rev 391

# Schema validation stub
# rev 406

# Schema validation stub
# rev 421

# Schema validation stub
# rev 436

# Schema validation stub
# rev 451

# Schema validation stub
# rev 466

# Schema validation stub
# rev 481

# Schema validation stub
# rev 496

# Schema validation stub
# rev 511

# Schema validation stub
# rev 526

# Schema validation stub
# rev 541

# Schema validation stub
# rev 556

# Schema validation stub
# rev 571

# Schema validation stub
# rev 586

# Schema validation stub
# rev 601

# Schema validation stub
# rev 616

# Schema validation stub
# rev 631

# Schema validation stub
# rev 646

# Schema validation stub
# rev 661

# Schema validation stub
# rev 676

# Schema validation stub
# rev 691

# Schema validation stub
# rev 706

# Schema validation stub
# rev 721

# Schema validation stub
# rev 736

# Schema validation stub
# rev 751

# Schema validation stub
# rev 766

# Schema validation stub
# rev 781

# Schema validation stub
# rev 796

# Schema validation stub
# rev 811

# Schema validation stub
# rev 826

# Schema validation stub
# rev 841

# Schema validation stub
# rev 856

# Schema validation stub
# rev 871

# Schema validation stub
# rev 886

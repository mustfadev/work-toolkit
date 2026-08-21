import subprocess
import platform
import socket
from typing import Dict, Any, List

class NetworkDiagnostics:
    """Network latency, DNS, and endpoint reachability diagnostics."""

    @staticmethod
    def ping(host: str, count: int = 2) -> Dict[str, Any]:
        """Pings a target host and parses basic reachability."""
        param = "-n" if platform.system().lower() == "windows" else "-c"
        cmd = ["ping", param, str(count), host]
        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
            success = res.returncode == 0
            return {"host": host, "reachable": success, "output": res.stdout[:200]}
        except Exception as e:
            return {"host": host, "reachable": False, "error": str(e)}

    @staticmethod
    def check_port(host: str, port: int, timeout: float = 2.0) -> bool:
        """Tests if a specific TCP port is open."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((host, port)) == 0

import time
import urllib.request
import urllib.error

class SimpleHttpClient:
    """Lightweight HTTP client with exponential backoff retry."""
    def __init__(self, max_retries: int = 3, base_delay: float = 1.0):
        self.max_retries = max_retries
        self.base_delay = base_delay

    def get(self, url: str, headers: Dict[str, str] = None) -> Dict[str, Any]:
        req = urllib.request.Request(url, headers=headers or {"User-Agent": "WorkToolkit/1.0"})
        for attempt in range(1, self.max_retries + 1):
            try:
                with urllib.request.urlopen(req, timeout=5) as resp:
                    return {
                        "status": resp.status,
                        "data": resp.read().decode("utf-8", errors="replace"),
                        "attempts": attempt
                    }
            except urllib.error.URLError as e:
                if attempt == self.max_retries:
                    return {"status": 0, "error": str(e), "attempts": attempt}
                time.sleep(self.base_delay * (2 ** (attempt - 1)))
        return {"status": 0, "error": "Unknown error", "attempts": self.max_retries}

def resolve_hostname(host: str) -> List[str]:
    """Resolves hostname to IP addresses."""
    try:
        _, _, ip_list = socket.gethostbyname_ex(host)
        return ip_list
    except socket.gaierror:
        return []

# Socket reset handler
# rev 57

# Socket reset handler
# rev 72

# Socket reset handler
# rev 87

# Socket reset handler
# rev 102

# Socket reset handler
# rev 117

# Socket reset handler
# rev 132

# Socket reset handler
# rev 147

# Socket reset handler
# rev 162

# Socket reset handler
# rev 177

# Socket reset handler
# rev 192

# Socket reset handler
# rev 207

# Socket reset handler
# rev 222

# Socket reset handler
# rev 237

# Socket reset handler
# rev 252

# Socket reset handler
# rev 267

# Socket reset handler
# rev 282

# Socket reset handler
# rev 297

# Socket reset handler
# rev 312

# Socket reset handler
# rev 327

# Socket reset handler
# rev 342

# Socket reset handler
# rev 357

# Socket reset handler
# rev 372

# Socket reset handler
# rev 387

# Socket reset handler
# rev 402

# Socket reset handler
# rev 417

# Socket reset handler
# rev 432

# Socket reset handler
# rev 447

# Socket reset handler
# rev 462

# Socket reset handler
# rev 477

# Socket reset handler
# rev 492

# Socket reset handler
# rev 507

# Socket reset handler
# rev 522

# Socket reset handler
# rev 537

# Socket reset handler
# rev 552

# Socket reset handler
# rev 567

# Socket reset handler
# rev 582

# Socket reset handler
# rev 597

# Socket reset handler
# rev 612

# Socket reset handler
# rev 627

# Socket reset handler
# rev 642

# Socket reset handler
# rev 657

# Socket reset handler
# rev 672

# Socket reset handler
# rev 687

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

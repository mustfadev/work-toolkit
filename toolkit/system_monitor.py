import os
import shutil
import platform
from typing import Dict, Any, List

class SystemMonitor:
    """Inspects CPU, RAM, and Disk resource utilization."""
    
    @staticmethod
    def get_os_info() -> Dict[str, str]:
        return {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor()
        }

    @staticmethod
    def get_disk_usage(path: str = "/") -> Dict[str, float]:
        """Returns disk stats in GB."""
        try:
            total, used, free = shutil.disk_usage(path)
            return {
                "total_gb": round(total / (1024 ** 3), 2),
                "used_gb": round(used / (1024 ** 3), 2),
                "free_gb": round(free / (1024 ** 3), 2),
                "percent_used": round((used / total) * 100, 1)
            }
        except Exception:
            return {"total_gb": 0.0, "used_gb": 0.0, "free_gb": 0.0, "percent_used": 0.0}

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

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

def get_system_load() -> Dict[str, Any]:
    if HAS_PSUTIL:
        mem = psutil.virtual_memory()
        return {
            "cpu_percent": psutil.cpu_percent(interval=0.1),
            "ram_used_gb": round((mem.total - mem.available) / (1024 ** 3), 2),
            "ram_total_gb": round(mem.total / (1024 ** 3), 2),
            "ram_percent": mem.percent
        }
    return {"cpu_percent": 0.0, "ram_used_gb": 0.0, "ram_total_gb": 0.0, "ram_percent": 0.0}

class AlertManager:
    def __init__(self, disk_threshold: float = 90.0, ram_threshold: float = 85.0):
        self.disk_threshold = disk_threshold
        self.ram_threshold = ram_threshold

    def check_alerts(self, disk_path: str = "/") -> List[str]:
        alerts = []
        disk = SystemMonitor.get_disk_usage(disk_path)
        if disk["percent_used"] >= self.disk_threshold:
            alerts.append(f"WARNING: Disk usage high ({disk['percent_used']}%) on {disk_path}")
            
        load = get_system_load()
        if load["ram_percent"] >= self.ram_threshold:
            alerts.append(f"WARNING: RAM usage high ({load['ram_percent']}%)")
            
        return alerts

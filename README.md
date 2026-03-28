# Work Toolkit

A collection of personal Python automation scripts and utilities for daily workflows.

## Modules
- File Organizer
- Data Cleaner
- System Monitor
- Backup Service

### File Organizer Usage
```python
from toolkit.file_organizer import FileOrganizer

organizer = FileOrganizer("~/Downloads")
report = organizer.organize(dry_run=False)
print("Files organized:", report)
```

### Data Cleaner Usage
```python
from toolkit.data_cleaner import DataSanitizer

email = DataSanitizer.validate_email(" user@DOMAIN.com ")
phone = DataSanitizer.format_phone("0555-123-456", default_country_code="+966")
print(email, phone)
```

### System Monitor Usage
```python
from toolkit.system_monitor import SystemMonitor, AlertManager

disk = SystemMonitor.get_disk_usage("C:\\")
alerts = AlertManager().check_alerts("C:\\")
print(f"Disk used: {disk['percent_used']}% | Alerts: {alerts}")
```

### Backup Manager Usage
```python
from toolkit.backup_service import BackupManager

mgr = BackupManager("./backups")
zip_path = mgr.create_zip_archive("./my_project")
mgr.rotate_backups(max_keep=3)
print("Backup created:", zip_path)
```

### Network Diagnostics Usage
```python
from toolkit.net_tools import NetworkDiagnostics, resolve_hostname

ping_res = NetworkDiagnostics.ping("1.1.1.1")
ips = resolve_hostname("google.com")
print("Ping result:", ping_res["reachable"], "IPs:", ips)
```

## CLI Interface
```bash
python cli.py organize ~/Downloads
python cli.py status
python cli.py password --length 20
python cli.py ping 8.8.8.8
```

<!-- Troubleshooting notes -->
# rev 64

<!-- Troubleshooting notes -->
# rev 79

<!-- Troubleshooting notes -->
# rev 94

<!-- Troubleshooting notes -->
# rev 109

<!-- Troubleshooting notes -->
# rev 124

<!-- Troubleshooting notes -->
# rev 139

<!-- Troubleshooting notes -->
# rev 154

<!-- Troubleshooting notes -->
# rev 169

<!-- Troubleshooting notes -->
# rev 184

<!-- Troubleshooting notes -->
# rev 199

<!-- Troubleshooting notes -->
# rev 214

<!-- Troubleshooting notes -->
# rev 229

<!-- Troubleshooting notes -->
# rev 244

<!-- Troubleshooting notes -->
# rev 259

<!-- Troubleshooting notes -->
# rev 274

<!-- Troubleshooting notes -->
# rev 289

<!-- Troubleshooting notes -->
# rev 304

<!-- Troubleshooting notes -->
# rev 319

<!-- Troubleshooting notes -->
# rev 334

<!-- Troubleshooting notes -->
# rev 349

<!-- Troubleshooting notes -->
# rev 364

<!-- Troubleshooting notes -->
# rev 379

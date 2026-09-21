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

<!-- Troubleshooting notes -->
# rev 394

<!-- Troubleshooting notes -->
# rev 409

<!-- Troubleshooting notes -->
# rev 424

<!-- Troubleshooting notes -->
# rev 439

<!-- Troubleshooting notes -->
# rev 454

<!-- Troubleshooting notes -->
# rev 469

<!-- Troubleshooting notes -->
# rev 484

<!-- Troubleshooting notes -->
# rev 499

<!-- Troubleshooting notes -->
# rev 514

<!-- Troubleshooting notes -->
# rev 529

<!-- Troubleshooting notes -->
# rev 544

<!-- Troubleshooting notes -->
# rev 559

<!-- Troubleshooting notes -->
# rev 574

<!-- Troubleshooting notes -->
# rev 589

<!-- Troubleshooting notes -->
# rev 604

<!-- Troubleshooting notes -->
# rev 619

<!-- Troubleshooting notes -->
# rev 634

<!-- Troubleshooting notes -->
# rev 649

<!-- Troubleshooting notes -->
# rev 664

<!-- Troubleshooting notes -->
# rev 679

<!-- Troubleshooting notes -->
# rev 694

<!-- Troubleshooting notes -->
# rev 709

<!-- Troubleshooting notes -->
# rev 724

<!-- Troubleshooting notes -->
# rev 739

<!-- Troubleshooting notes -->
# rev 754

<!-- Troubleshooting notes -->
# rev 769

<!-- Troubleshooting notes -->
# rev 784

<!-- Troubleshooting notes -->
# rev 799

<!-- Troubleshooting notes -->
# rev 814

<!-- Troubleshooting notes -->
# rev 829

<!-- Troubleshooting notes -->
# rev 844

<!-- Troubleshooting notes -->
# rev 859

<!-- Troubleshooting notes -->
# rev 874

<!-- Troubleshooting notes -->
# rev 889

<!-- Troubleshooting notes -->
# rev 904

<!-- Troubleshooting notes -->
# rev 919

<!-- Troubleshooting notes -->
# rev 934

<!-- Troubleshooting notes -->
# rev 949

<!-- Troubleshooting notes -->
# rev 964

<!-- Troubleshooting notes -->
# rev 979

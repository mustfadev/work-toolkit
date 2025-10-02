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

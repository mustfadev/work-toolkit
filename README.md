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

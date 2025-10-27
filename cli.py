import argparse
import sys
from toolkit.file_organizer import FileOrganizer
from toolkit.system_monitor import SystemMonitor, format_system_summary
from toolkit.crypto_vault import CryptoHelper
from toolkit.net_tools import NetworkDiagnostics

def main():
    parser = argparse.ArgumentParser(description="Work Toolkit - Personal Productivity Automations")
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to execute")

    p_org = subparsers.add_parser("organize", help="Organize files in directory")
    p_org.add_argument("path", help="Target folder path")
    p_org.add_argument("--dry-run", action="store_true", help="Simulate without moving")

    subparsers.add_parser("status", help="Show system status summary")

    p_key = subparsers.add_parser("password", help="Generate secure password")
    p_key.add_argument("--length", type=int, default=16)

    p_ping = subparsers.add_parser("ping", help="Ping a remote host")
    p_ping.add_argument("host", help="Hostname or IP")

    args = parser.parse_args()

    if args.command == "organize":
        org = FileOrganizer(args.path)
        res = org.organize(dry_run=args.dry_run)
        print("Organization results:", res)
    elif args.command == "status":
        print(format_system_summary())
    elif args.command == "password":
        pwd = CryptoHelper.generate_password(args.length)
        print("Generated password:", pwd)
    elif args.command == "ping":
        r = NetworkDiagnostics.ping(args.host)
        print("Reachability:", r["reachable"])
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

# Backup command support
def add_backup_subparser(subparsers):
    p = subparsers.add_parser("backup", help="Create zip backup of directory")
    p.add_argument("source", help="Source folder to backup")
    p.add_argument("--dest", default="./backups", help="Destination folder")

# --verbose option
# rev 67

# --verbose option
# rev 82

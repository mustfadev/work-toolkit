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

# --verbose option
# rev 97

# --verbose option
# rev 112

# --verbose option
# rev 127

# --verbose option
# rev 142

# --verbose option
# rev 157

# --verbose option
# rev 172

# --verbose option
# rev 187

# --verbose option
# rev 202

# --verbose option
# rev 217

# --verbose option
# rev 232

# --verbose option
# rev 247

# --verbose option
# rev 262

# --verbose option
# rev 277

# --verbose option
# rev 292

# --verbose option
# rev 307

# --verbose option
# rev 322

# --verbose option
# rev 337

# --verbose option
# rev 352

# --verbose option
# rev 367

# --verbose option
# rev 382

# --verbose option
# rev 397

# --verbose option
# rev 412

# --verbose option
# rev 427

# --verbose option
# rev 442

# --verbose option
# rev 457

# --verbose option
# rev 472

# --verbose option
# rev 487

# --verbose option
# rev 502

# --verbose option
# rev 517

# --verbose option
# rev 532

# --verbose option
# rev 547

# --verbose option
# rev 562

# --verbose option
# rev 577

# --verbose option
# rev 592

# --verbose option
# rev 607

# --verbose option
# rev 622

# --verbose option
# rev 637

# --verbose option
# rev 652

# --verbose option
# rev 667

# --verbose option
# rev 682

# --verbose option
# rev 697

# --verbose option
# rev 712

# --verbose option
# rev 727

# --verbose option
# rev 742

# --verbose option
# rev 757

# --verbose option
# rev 772

# --verbose option
# rev 787

# --verbose option
# rev 802

# --verbose option
# rev 817

# --verbose option
# rev 832

# --verbose option
# rev 847

# --verbose option
# rev 862

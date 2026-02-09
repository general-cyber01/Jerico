#!/usr/bin/env python3
"""Jerico - Linux Host Monitoring & Detection Tool"""
import sys
from typing import NoReturn

from jerico.cli import parse_args
from jerico.scanner.disk import scan_disk
from jerico.scanner.process import scan_processes
from jerico.utils.privilege import require_root

# Constants
BANNER = r"""
     ██╗███████╗██████╗ ██╗ ██████╗ ██████╗ 
     ██║██╔════╝██╔══██╗██║██╔════╝██╔═══██╗
     ██║█████╗  ██████╔╝██║██║     ██║   ██║
██   ██║██╔══╝  ██╔══██╗██║██║     ██║   ██║
╚█████╔╝███████╗██║  ██║██║╚██████╗╚██████╔╝
 ╚════╝ ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ 
      Linux Host Monitoring & Detection Tool
              Created by Abdmalik
"""


def print_banner() -> None:
    """Display the Jerico banner."""
    print(BANNER)


def run_scan(args) -> None:
    """Execute the appropriate scan based on command-line arguments.
    
    Args:
        args: Parsed command-line arguments
    """
    if args.all:
        print("[*] Running full system scan...")
        scan_processes(verbose=True)
        scan_disk()
    elif args.process:
        print("[*] Scanning processes...")
        scan_processes(verbose=True)
    elif args.disk:
        print("[*] Scanning disk...")
        scan_disk()
    else:
        print("[*] Running light scan...")
        scan_processes()


def main() -> NoReturn:
    """Main entry point for Jerico."""
    require_root()
    args = parse_args()
    print_banner()
    
    try:
        run_scan(args)
    except KeyboardInterrupt:
        print("\n[!] Jerico scan stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] Scan failed: {e}")
        sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()

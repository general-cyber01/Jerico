#!/usr/bin/env python3
"""
Jerico - Linux Host Monitoring & Detection Tool
Author: Abdullahi Abdmaleek
"""

import sys
from typing import NoReturn

from jerico.cli import parse_args
from jerico.scanner.disk import scan_disk
from jerico.scanner.process import scan_processes
from jerico.utils.privilege import require_root

# Banner for Jerico
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
    """
    Execute scans based on parsed CLI arguments.

    Args:
        args: Parsed command-line arguments
    """
    if args.all:
        print("[*] Running full system scan (processes + disk)...")
        scan_processes(verbose=True)
        scan_disk()
    elif args.process:
        print("[*] Scanning processes...")
        scan_processes(verbose=True)
    elif args.disk:
        print("[*] Scanning disk...")
        scan_disk()
    else:
        print("[*] Running light process scan by default...")
        scan_processes()


def main() -> NoReturn:
    """Main entry point for Jerico."""
    # Ensure the user is root
    require_root()

    # Parse CLI arguments
    args = parse_args()

    # Print banner
    print_banner()

    # Run the scans
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

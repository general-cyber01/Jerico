#!/usr/bin/env python3
"""
Jerico - Linux Host Monitoring & Detection Tool v1.1
Author: Abdullahi Abdmaleek
"""

import sys
import threading
from typing import NoReturn

from jerico.cli import parse_args
from jerico.scanner.disk import scan_disk
from jerico.scanner.process import scan_processes
from jerico.utils.privilege import require_root

# Banner
BANNER = r"""
     ██╗███████╗██████╗ ██╗ ██████╗ ██████╗ 
     ██║██╔════╝██╔══██╗██║██╔════╝██╔═══██╗
     ██║█████╗  ██████╔╝██║██║     ██║   ██║
██   ██║██╔══╝  ██╔══██╗██║██║     ██║   ██║
╚█████╔╝███████╗██║  ██║██║╚██████╗╚██████╔╝
 ╚════╝ ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ 
      Robust Linux Host Monitoring & Detection Tool
              Created by Abdmalik
              V1.0
"""


def print_banner() -> None:
    """Display the Jerico banner."""
    print(BANNER)


def run_scan(args) -> None:
    """Execute scans based on CLI arguments."""
    if args.all:
        print("[*] Running full system scan...")
        # Run process scan in a separate thread
        t = threading.Thread(target=scan_processes, kwargs={'verbose': True})
        t.start()
        # Run disk scan concurrently
        scan_disk()
        t.join()
    elif args.process:
        scan_processes(verbose=True)
    elif args.disk:
        scan_disk()
    else:
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

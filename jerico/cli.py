#!/usr/bin/env python3

import argparse
from jerico.main import run_all, run_process_scan, run_disk_scan


def main():
    parser = argparse.ArgumentParser(
        description="Jerico – Lightweight Linux Host Monitoring Tool"
    )

    parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="Run full system scan"
    )

    parser.add_argument(
        "-p", "--process",
        action="store_true",
        help="Scan running processes"
    )

    parser.add_argument(
        "-d", "--disk",
        action="store_true",
        help="Scan disk for large/suspicious files"
    )

    args = parser.parse_args()

    # If no argument is provided
    if not any(vars(args).values()):
        parser.print_help()
        return

    if args.all:
        run_all()

    if args.process:
        run_process_scan()

    if args.disk:
        run_disk_scan()


if __name__ == "__main__":
    main()

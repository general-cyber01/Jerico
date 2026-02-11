#!/usr/bin/env python3
"""
Jerico CLI – Argument parser for Linux Host Monitoring Tool
Author: Abdullahi Abdmaleek
"""

import argparse


def parse_args():
    """
    Parse command-line arguments for Jerico.

    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Jerico – Lightweight Linux Host Monitoring Tool"
    )

    parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="Run full system scan (processes + disk)"
    )

    parser.add_argument(
        "-p", "--process",
        action="store_true",
        help="Scan running processes only"
    )

    parser.add_argument(
        "-d", "--disk",
        action="store_true",
        help="Scan disk for large/suspicious files only"
    )

    return parser.parse_args()

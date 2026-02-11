#!/usr/bin/env python3
"""
Disk Scanner Module
Author: Abdullahi Abdmaleek
"""

import os
from pathlib import Path
from datetime import datetime, timedelta

def scan_disk():
    """
    Scan disk recursively for:
    - Large files (>100MB)
    - Recently modified files (<7 days)
    - Suspicious file types (.exe, .sh, .py)
    """
    print("[*] Starting robust disk scan...")

    scan_paths = ["/"]  # Can be extended to all mount points
    large_files = []
    recent_files = []
    suspicious_extensions = [".exe", ".sh", ".py"]

    for base_path in scan_paths:
        for root, dirs, files in os.walk(base_path):
            for file in files:
                try:
                    file_path = Path(root) / file
                    size_mb = file_path.stat().st_size / (1024 * 1024)
                    mtime = datetime.fromtimestamp(file_path.stat().st_mtime)

                    # Large files
                    if size_mb > 100:
                        large_files.append((file_path, size_mb))

                    # Recently modified files
                    if mtime > datetime.now() - timedelta(days=7):
                        recent_files.append((file_path, mtime))

                    # Suspicious file types
                    if file_path.suffix in suspicious_extensions:
                        print(f"[!] Suspicious file detected: {file_path}")

                except Exception:
                    continue

    print(f"[*] Large files (>100MB): {len(large_files)}")
    for f, size in large_files:
        print(f" - {f} ({size:.2f} MB)")

    print(f"[*] Recently modified files (<7 days): {len(recent_files)}")
    for f, mtime in recent_files:
        print(f" - {f} modified at {mtime}")

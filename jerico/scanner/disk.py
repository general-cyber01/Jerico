#!/usr/bin/env python3
"""Disk scanner module for Jerico."""
import os
import sys
from pathlib import Path
from typing import List, Tuple

# Constants
EXCLUDE_DIRS = frozenset(["/proc", "/sys", "/dev", "/run", "/snap"])
SCAN_PROGRESS_INTERVAL = 1000  # Report progress every N files
MB = 1024 ** 2
GB = 1024 ** 3


def format_size(size_bytes: int) -> str:
    """Format file size in human-readable format.
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        Formatted size string (e.g., "1.5 GB", "234.5 MB")
    """
    if size_bytes >= GB:
        return f"{size_bytes / GB:.2f} GB"
    elif size_bytes >= MB:
        return f"{size_bytes / MB:.2f} MB"
    elif size_bytes >= 1024:
        return f"{size_bytes / 1024:.2f} KB"
    else:
        return f"{size_bytes} B"


def should_skip_directory(root: str) -> bool:
    """Check if directory should be skipped during scan.
    
    Args:
        root: Directory path to check
        
    Returns:
        True if directory should be skipped
    """
    return any(root.startswith(excluded) for excluded in EXCLUDE_DIRS)


def scan_disk(paths: Tuple[str, ...] = ("/",), limit: int = 10, verbose: bool = True) -> List[Tuple[int, str]]:
    """Scan filesystem for large files.
    
    Args:
        paths: Tuple of root paths to scan
        limit: Number of largest files to display
        verbose: Whether to print progress and results
        
    Returns:
        List of (size, filepath) tuples sorted by size (largest first)
    """
    if verbose:
        print("[*] Scanning disk for large files...")
    
    files: List[Tuple[int, str]] = []
    scanned = 0
    errors = 0
    
    try:
        for base in paths:
            if not os.path.exists(base):
                if verbose:
                    print(f"[!] Warning: Path does not exist: {base}")
                continue
                
            for root, dirs, filenames in os.walk(base, topdown=True):
                # Skip excluded directories
                if should_skip_directory(root):
                    dirs[:] = []  # Don't descend into subdirectories
                    continue
                
                # Filter out excluded subdirectories
                dirs[:] = [d for d in dirs if not should_skip_directory(os.path.join(root, d))]
                
                for name in filenames:
                    try:
                        full_path = os.path.join(root, name)
                        
                        # Use lstat to avoid following symlinks
                        stat_info = os.lstat(full_path)
                        
                        # Skip if it's a symlink or not a regular file
                        if not os.path.isfile(full_path) or os.path.islink(full_path):
                            continue
                        
                        size = stat_info.st_size
                        files.append((size, full_path))
                        scanned += 1
                        
                        if verbose and scanned % SCAN_PROGRESS_INTERVAL == 0:
                            print(f"\r[*] Files scanned: {scanned:,}", end="", flush=True)
                    
                    except (PermissionError, FileNotFoundError, OSError):
                        errors += 1
                        continue
        
        if verbose:
            print(f"\n[*] Disk scan complete - {scanned:,} files scanned, {errors:,} errors")
        
        # Sort by size (largest first) - use partial sort for better performance
        if limit < len(files):
            # Partial sort using heapq for large datasets
            import heapq
            largest_files = heapq.nlargest(limit, files, key=lambda x: x[0])
        else:
            largest_files = sorted(files, reverse=True)
        
        if verbose and largest_files:
            print(f"\n[*] Top {min(limit, len(largest_files))} largest files:")
            for size, filepath in largest_files[:limit]:
                print(f"    {format_size(size):>10} → {filepath}")
        
        return largest_files
    
    except KeyboardInterrupt:
        if verbose:
            print("\n[!] Disk scan interrupted by user.")
        sys.exit(0)


def main():
    """CLI entry point for standalone disk scanning."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Scan disk for large files")
    parser.add_argument("-p", "--paths", nargs="+", default=["/"], help="Paths to scan")
    parser.add_argument("-l", "--limit", type=int, default=10, help="Number of files to display")
    args = parser.parse_args()
    
    scan_disk(paths=tuple(args.paths), limit=args.limit)


if __name__ == "__main__":
    main()

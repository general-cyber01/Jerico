import os
import sys

EXCLUDE_DIRS = ("/proc", "/sys", "/dev", "/run")

def scan_disk(paths=("/",), limit=10):
    print("[*] Scanning disk for large files...")

    files = []
    scanned = 0

    try:
        for base in paths:
            for root, dirs, filenames in os.walk(base, topdown=True):

                if root.startswith(EXCLUDE_DIRS):
                    dirs[:] = []
                    continue

                for name in filenames:
                    try:
                        full_path = os.path.join(root, name)
                        size = os.path.getsize(full_path)
                        files.append((size, full_path))
                        scanned += 1

                        if scanned % 500 == 0:
                            print(f"\r[*] Files scanned: {scanned}", end="")
                    except:
                        continue

        print("\n[*] Disk scan complete")

        files.sort(reverse=True)
        print("\n[*] Largest files found:")
        for size, file in files[:limit]:
            print(f"    {size / (1024**2):.2f} MB → {file}")

    except KeyboardInterrupt:
        print("\n[!] Disk scan interrupted by user.")
        sys.exit(0)


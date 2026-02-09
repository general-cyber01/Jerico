import os
import sys

def require_root():
    if os.geteuid() != 0:
        print("[!] Jerico must be run as root.")
        sys.exit(1)


import sys
from jerico.cli import parse_args
from jerico.utils.privilege import require_root
from jerico.scanner.process import scan_processes
from jerico.scanner.disk import scan_disk

def print_banner():
    print(r"""
     ██╗███████╗██████╗ ██╗ ██████╗ ██████╗ 
     ██║██╔════╝██╔══██╗██║██╔════╝██╔═══██╗
     ██║█████╗  ██████╔╝██║██║     ██║   ██║
██   ██║██╔══╝  ██╔══██╗██║██║     ██║   ██║
╚█████╔╝███████╗██║  ██║██║╚██████╗╚██████╔╝
 ╚════╝ ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ 

      Linux Host Monitoring & Detection Tool
              Created by Abdmalik
    """)


def main():
    require_root()
    args = parse_args()

    print_banner()

    try:
        if args.all:
            scan_processes(verbose=True)
            scan_disk()
        elif args.process:
            scan_processes(verbose=True)
        elif args.disk:
            scan_disk()
        else:
            print("[*] Running light scan...")
            scan_processes()

    except KeyboardInterrupt:
        print("\n[!] Jerico scan stopped by user.")
        sys.exit(0)


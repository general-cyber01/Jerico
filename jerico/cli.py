import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Jerico – Lightweight Linux Host Monitoring Tool"
    )

    parser.add_argument("-a", "--all", action="store_true", help="Run full scan")
    parser.add_argument("-p", "--process", action="store_true", help="Process scan")
    parser.add_argument("-d", "--disk", action="store_true", help="Disk scan")
    parser.add_argument("-m", "--memory", action="store_true", help="Memory scan (coming soon)")

    return parser.parse_args()


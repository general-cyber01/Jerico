#!/usr/bin/env python3
"""
Process Scanner Module
Author: Abdullahi Abdmaleek
"""

import psutil
import time

def scan_processes(verbose=False, interval=5):
    """
    Display running processes dynamically, like ps aux.

    Args:
        verbose (bool): if True, refreshes continuously
        interval (int): refresh interval in seconds
    """
    try:
        while True:
            print("\n[*] Running processes snapshot")
            print(f"{'PID':<8}{'USER':<12}{'CPU%':<6}{'MEM%':<6}{'CMD'}")
            for proc in psutil.process_iter(['pid', 'username', 'cpu_percent', 'memory_percent', 'cmdline']):
                try:
                    pid = proc.info['pid']
                    user = proc.info['username']
                    cpu = proc.info['cpu_percent']
                    mem = proc.info['memory_percent']
                    cmd = " ".join(proc.info['cmdline']) if proc.info['cmdline'] else ""
                    print(f"{pid:<8}{user:<12}{cpu:<6}{mem:<6.2f}{cmd}")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            if not verbose:
                break
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[!] Process scan stopped by user.")

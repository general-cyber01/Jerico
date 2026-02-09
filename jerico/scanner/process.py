import os

def scan_processes(verbose=False):
    print("[*] Scanning running processes...")

    suspicious = []
    processes = []

    for pid in os.listdir("/proc"):
        if not pid.isdigit():
            continue

        try:
            with open(f"/proc/{pid}/comm", "r") as f:
                name = f.read().strip()

            exe = os.readlink(f"/proc/{pid}/exe")

            processes.append((pid, name, exe))

            if "(deleted)" in exe or exe.startswith(("/tmp", "/dev/shm")):
                suspicious.append((pid, name, exe))

        except:
            continue

    if verbose:
        print("\nPID\tPROCESS\tPATH")
        print("-" * 70)
        for pid, name, exe in processes[:25]:
            print(f"{pid}\t{name}\t{exe}")

    if suspicious:
        print("\n[!] Suspicious activity detected:")
        for pid, name, exe in suspicious:
            print(f"    PID {pid} ({name}) → {exe}")
    else:
        print("\n[✓] No suspicious processes found.")


#!/usr/bin/env python3

import os
import sys
import shutil

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True is there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def main():
    checks = [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full."),
    ]

    everything_ok = True

    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False
            sys.exit(1)

    if not everything_ok:
        sys.exit(1)
    else:
        print("Everything ok.")
        sys.exit(0)

main()
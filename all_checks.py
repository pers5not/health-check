#!/usr/bin/env python3

import os
import sys
import shutil



def check_reboot():
    """Returns True if the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")


def check_disk_full(disk, min_absolute, min_percent):
    """Return True if there isn't enougth disk space, False otherwise"""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gygabates
    gygabates_free = du.free / 2 ** 30
    if percent_free < min_percent or gygabates_free < min_absolute:
        return True
    return False


def main():
    if check_reboot():
        print("Pending reboot")
        sys.exit(1)
    if check_disk_full(disk='/', min_absolute=2, min_percent=10):
        print("Disk Full.")
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)

main()

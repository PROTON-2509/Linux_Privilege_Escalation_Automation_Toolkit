import time

from modules.system_info import get_system_info
from modules.suid_scanner import scan_suid
from modules.writable_scanner import scan_writable
from modules.cron_scanner import scan_cron
from modules.sudo_scanner import check_sudo
from modules.kernel_scanner import check_kernel
from modules.report_generator import generate_report


def banner():
    print("""
=====================================================================================================
                                     Linux Privilege Escalation Toolkit
                                          Automated Enumeration Tool                      By:- PROTON
=====================================================================================================
""")


def main():

    start = time.time()

    banner()

    system_info = get_system_info()
    suid = scan_suid()
    writable = scan_writable()
    cron = scan_cron()
    sudo = check_sudo()
    kernel = check_kernel()

    generate_report(system_info, suid, writable, cron, sudo, kernel)

    end = time.time()
    print(f"\nScan completed in {round(end-start,2)} seconds")


if __name__ == "__main__":
    main()

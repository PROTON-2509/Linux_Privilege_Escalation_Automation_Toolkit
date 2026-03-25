def generate_report(system_info, suid, writable, cron, sudo, kernel):

    print("\n\n===== PRIVILEGE ESCALATION REPORT =====\n")

    print("SYSTEM INFORMATION")
    print("------------------")

    for key, value in system_info.items():
        print(f"{key}: {value}")

    print("\n--- Findings ---\n")

    print(f"[MEDIUM] SUID binaries found: {len(suid)}")

    print(f"[HIGH] World writable files: {len(writable)}")

    if "root" in cron:
        print("[MEDIUM] Cron jobs running as root detected")

    if "NOPASSWD" in sudo:
        print("[CRITICAL] Dangerous sudo configuration detected")

    print("\nKernel Info:")
    print(kernel)

    print("\n===== END OF REPORT =====\n")

    with open("scan_report.txt", "w") as report:

        report.write("Linux Privilege Escalation Toolkit Report\n\n")

        for key, value in system_info.items():
            report.write(f"{key}: {value}\n")

        report.write(f"\nSUID binaries found: {len(suid)}")
        report.write(f"\nWorld writable files: {len(writable)}")

        report.write("\n\nKernel Information:\n")
        report.write(kernel)

        report.write("\n\nSudo Configuration:\n")
        report.write(sudo)

    print("Report saved as scan_report.txt")

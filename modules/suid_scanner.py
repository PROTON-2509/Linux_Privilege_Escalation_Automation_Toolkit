import subprocess

gtfobins = [
    "awk", "bash", "find", "perl", "python", "ruby",
    "vim", "less", "nano", "cp", "mv", "tar"
]


def scan_suid():

    print("\n[+] Scanning for SUID binaries...\n")

    try:

        result = subprocess.run(
            "find / -perm -4000 -type f 2>/dev/null",
            shell=True,
            capture_output=True,
            text=True
        )

        suid_files = result.stdout.splitlines()

        for file in suid_files[:20]:

            print(file)

            for binary in gtfobins:
                if binary in file:
                    print(f"   [!] Potential GTFOBins exploitation: {binary}")

        if len(suid_files) > 20:
            print("\nShowing first 20 results...")

        return suid_files

    except Exception as e:
        print("Error scanning SUID:", e)
        return []



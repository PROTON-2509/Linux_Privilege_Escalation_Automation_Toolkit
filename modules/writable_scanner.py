import subprocess


def scan_writable():

    print("\n[+] Scanning for world-writable files...\n")

    try:

        result = subprocess.run(
            "find / -path /proc -prune -o -type f -writable -print 2>/dev/null",
            shell=True,
            capture_output=True,
            text=True
        )

        files = result.stdout.splitlines()

        for file in files[:20]:
            print(file)

        if len(files) > 20:
            print("\nShowing first 20 results...")

        return files

    except Exception as e:
        print("Error scanning writable files:", e)
        return []

import subprocess


def scan_cron():

    print("\n[+] Scanning Cron Jobs...\n")

    try:

        result = subprocess.check_output(
            "cat /etc/crontab",
            shell=True,
            text=True
        )

        print(result)

        return result

    except Exception as e:
        print("Error scanning cron:", e)
        return ""

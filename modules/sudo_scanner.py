import subprocess


def check_sudo():

    print("\n[+] Checking Sudo Permissions...\n")

    try:

        result = subprocess.check_output(
            "sudo -l",
            shell=True,
            text=True
        )

        print(result)

        return result

    except Exception as e:
        print("Error checking sudo:", e)
        return ""

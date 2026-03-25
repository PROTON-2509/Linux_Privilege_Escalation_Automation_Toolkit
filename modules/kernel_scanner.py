import subprocess


def check_kernel():

    print("\n[+] Checking Kernel Version...\n")

    try:

        result = subprocess.check_output(
            "uname -a",
            shell=True,
            text=True
        )

        print(result)

        return result

    except Exception as e:
        print("Error checking kernel:", e)
        return ""


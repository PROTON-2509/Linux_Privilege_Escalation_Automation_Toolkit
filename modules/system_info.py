import platform
import socket
import os
import subprocess


def get_system_info():

    print("\n[+] Collecting System Information...\n")

    try:
        ip = subprocess.check_output("hostname -I", shell=True, text=True).strip()
    except:
        ip = "Unable to detect"

    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Hostname": socket.gethostname(),
        "IP Address": ip,
        "User": os.getlogin()
    }

    for key, value in info.items():
        print(f"{key}: {value}")

    return info

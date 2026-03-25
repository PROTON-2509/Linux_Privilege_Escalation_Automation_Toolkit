# Linux Privilege Escalation Toolkit

A modular Linux privilege escalation enumeration toolkit developed in Python to assist security researchers and penetration testers in identifying potential privilege escalation vectors on Linux systems.
This toolkit automates common checks such as SUID binaries, sudo permissions, cron jobs, writable files, and kernel information to help identify misconfigurations that may allow a user to gain elevated privileges.

### PROJECT OVERVIEW

Privilege escalation is one of the most important phases in a penetration test. After gaining an initial foothold on a system, attackers attempt to escalate their privileges to gain root access.
This project was developed as part of a cybersecurity academic project to demonstrate how automated tools can help detect common Linux privilege escalation opportunities.

### FEATURES

• System information enumeration  
• Kernel version detection  
• SUID binary discovery  
• Writable file and directory detection  
• Sudo permission enumeration  
• Cron job analysis  
• Modular scanning architecture  
• Color-coded terminal output for better readability  

### USAGE

Run the toolkit using Python:

python3 main.py

The toolkit will automatically execute all scanning modules and display the results.

### EXAMPLE OUTPUT

=========================================
   Linux Privilege Escalation Toolkit
=========================================

[+] Gathering System Information  
OS: Linux  
Kernel Version: 2.6.24  

[+] Scanning for SUID binaries  
/usr/bin/passwd  
/usr/bin/sudo  

[+] Checking sudo permissions  
User may run the following commands:  
(root) NOPASSWD: /usr/bin/vim  

[+] Scanning cron jobs  
/etc/crontab found  

Scan completed successfully.

=========================================
=========================================

### TECHNOLOGIES USED

• Python  
• Linux  
• Bash commands  
• Python subprocess module  

### EDUCATIONAL PURPOSE

This toolkit was developed strictly for educational and research purposes as part of a cybersecurity academic project.
It should only be used in authorized environments such as penetration testing labs or vulnerable machines like Metasploitable 2.
Unauthorized use against systems without permission is illegal.

### FUTURE IMPROVEMENTS

• Automated exploit suggestion  
• Kernel vulnerability database integration  
• Improved reporting system  
• JSON or HTML report generation  
• Additional privilege escalation checks  

### AUTHOR

Krishna Tambare  
B.Tech Computer Science Engineering

### LICENSE
This project is intended for educational use and cybersecurity learning.

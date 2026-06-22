#!/usr/bin/env python3

import subprocess

target = input("Enter Target Domain: ")

report = f"{target}_report.txt"

def recon(target):

	get_ip = subprocess.run(f"host {target} | grep address | awk '{{print $4}}'", shell=True, capture_output=True, text=True)

	mail_mx = subprocess.run(f"dig MX {target} +short | awk '{{print $2}}'", shell=True, capture_output=True, text=True)

	httpx = subprocess.run(f"curl -I {target} | grep -E 'Server|Content-Type|Connection'", shell=True, capture_output=True, text=True)

	ping_check = subprocess.run(f"ping -c 3 {target} | grep loss", shell=True, capture_output=True, text=True)

	whois_check = subprocess.run(f"whois {target} | grep -E '^Registrar|^Creation Date|^Expiry Date' | tr -d ' ' | sort -u ", shell=True, capture_output=True, text=True)


	with open (report, "w") as file:
		file.write(f"{"="*10}\nRECON REPORT\n{"="*10}\nYour Target: {target} Recon Summary Report.\n{"="*3}> IP Address\n{get_ip.stdout}\n{"="*3}> Mail MX\n{mail_mx.stdout}\n{"="*3}> HTTP Header Info\n{httpx.stdout}\n{"="*3}> Check PING\n{ping_check.stdout}\n{"="*3}> WHOIS Info\n{whois_check.stdout}")

	print(f"Your recon on domain {target}, report saved successfully in file report.txt")

recon(target)

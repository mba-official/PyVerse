#!/usr/bin/env python3

import subprocess


report = "report.txt"

target = input("Enter Target Domain: ")

def recon(target):

	get_ip = subprocess.run(f"host {target} | grep address | awk '{{print $4}}'", shell=True, capture_output=True, text=True)

	mail_mx = subprocess.run(f"dig MX {target} +short | awk '{{print $2}}'", shell=True, capture_output=True, text=True)

	httpx = subprocess.run(f"curl -I {target} | grep -E 'Server|Content-Type|Connection'", shell=True, capture_output=True, text=True)

	ping_check = subprocess.run(f"ping -c 3 {target} | grep loss", shell=True, capture_output=True, text=True)

	whois_check = subprocess.run(f"whois {target} | grep -E 'Registrar URL|Creation Date|Expiry Date' | awk '!seen[\\$0]++' ", shell=True, capture_output=True, text=True)

	print(whois_check.stdout)

	# with open (report, "a") as file:
	# 	file.write(f"{"*"*10} RECON REPORT {"*"*10}\n{"="*3}> IP Address\n{get_ip.stdout}\n{"="*3}> Mail MX\n{mail_mx.stdout}\n{"="*3}> HTTP Header Info\n{httpx.stdout}")


recon(target)

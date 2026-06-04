#!/usr/bin/env python3

import time


endpoints = ["login", "admin", "dashboard", "register", "profile", "robots.txt"]
protocols = ["http", "https"]

def banner():
	print("="*15)
	print("Mini Recon Tool\nAuthor: Lazy Bear\nLicense: Free for educational purpose.\nTerms: Do not use this tool for illegal or unethical activities.\nStay Safe and Keep Learning")
	print("="*50)


def url_build():
	while True:
		domain = input("Enter the domain (Press Q for exist): ").lower().strip()

		if domain == 'q':
			print(f"{"-"*2}> Program exit successfully.")
			break

		user_protocol = input("Enter the protocol: ").lower().strip()

		if not domain or not user_protocol:
			print("Both field are required.")
			continue

		if user_protocol in protocols:
			print(f"{"-"*2}> Generating URL...")
			time.sleep(2)
			for i in endpoints:
				print(f"{user_protocol}://{domain}/{i}")
			print(f"{"-"*2}> URL Successfully Generated.")
			break
		else:
			print("Choose the correct protocol (http or https).")
			continue

def ending():
	print("="*50)
	print("Thanks for using.\nFollow me on github/lazy_bear.")


banner()
url_build()
ending()
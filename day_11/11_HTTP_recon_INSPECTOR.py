#!/usr/bin/env python3

import requests
from lxml.html import fromstring

def recon(domain):

	if domain == "":
		print("Domain is required.")
		return None
	if not domain.startswith(("http", "https")):
		domain = "https://"+domain

	custom_header = ["server", "host", "user-agent", "accept", "content-type", "content-length", "etag", "access-aontrol-allow-origin"]

	# print("this is fine 01.") Debugger
	
	try:
		# print("this is fine 0.") Debugger

		response = requests.get(domain, timeout=5)

		# print("this is fine 1.") Debugger
		# print(response) Debugger

		get_title = fromstring(response.content)
		title = get_title.findtext('.//title')

		print(f"URL: {response.url}\nStatus Code: {response.status_code}\nWebsite Title: {title}\nResponse Time: {response.elapsed}")

		# print("this is fine 2.") Debugger

		print(f"{"="*5} Header Information {"="*5}")
		for header in custom_header:
			output = response.headers.get(header)
			if output == None:
				print(f"{header}: Not Present")
			else:
				print(f"{header}: {output}")

		# print("this is fine 3.") Debugger

	except Exception as e:
		print("Error:",e)

domain = input("Enter the domain: ").lower().strip()

recon(domain)


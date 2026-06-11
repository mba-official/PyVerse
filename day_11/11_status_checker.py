#!/usr/bin/env python3

import requests


def check_status(domain):
	try:
		response = requests.get(domain)
		# print(response) Just to check if its working or not.

		url = response.url
		print(f"URL: {url}")
		
		status = response.status_code
		print(f"Status Code: {status}")

		text = response.text[0:100]
		print(f"Body Text: {text}")

		header = response.headers
		print(f"Header Info: {header}")		

	except Exception as e:
		print("Error:",e)
		return None

domain = input("Enter the URL: ").lower().strip()

check_status(domain)


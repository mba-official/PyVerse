#!/usr/bin/env python3

import requests

def custom_headers(domain):

	if domain == "":
		print("Domain is required.")
		return None
	if not domain.startswith("https"):
		domain = "https://"+domain

	try:
		response = requests.get(domain)
		print(f"URL: {response.url}")
		
		server = response.headers.get("server")
		content_type = response.headers.get("content-type")
		x_runtime = response.headers.get("x-runtime")
		etag = response.headers.get("etag")
		
		print(f"{"="*5} Header Information {"="*5}")
		print(f"Server: {server}\nContent-Type: {content_type}\nX-Runtime: {x_runtime}\nEtag: {etag}")

	except Exception as e:
		print("Error:",e)
		return None

domain = input("Enter the domain: ").lower().strip()

custom_headers(domain)


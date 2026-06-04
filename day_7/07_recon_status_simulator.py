#!/usr/bin/env python3


endpoints = {
				"login" : "200 Ok",
				"dashboard" : "403 Forbidden", 
				"register" : "200 Ok", 
				"contact-us" : "200 Ok", 
				"about" : "200 Ok",
				"home" : "200 Ok", 
				"robots.txt" : "403 Forbidden",
				"admin" : "404 Forbidden"
			}

protocols = ["http", "https"]


while True:
	domain = input("Enter the domain: ").lower().strip()
	user_protocol = input("Enter the protocol (http or https): ").lower().strip()

	if domain == "" or user_protocol == "":
		print("Both field are required.")
		continue

	if user_protocol in protocols:
		print("="*30)
		print("Generated endpoints are given below with status code:")
		for key in endpoints:
			print(f"{user_protocol}://{domain}/{key}, status code: [{endpoints[key]}]")
		print("="*30)
	else:
		print("Invalid Protocol. Correct protocol (http or https).")
		continue

	break


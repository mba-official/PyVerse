#!/usr/bin/env python3


endpoints = ["login", "dashboard", "register", "contact-us", "about", "home", "robot.txt"]
protocols = ["http", "https"]


while True:
	domain = input("Enter the domain: ").lower().strip()
	user_protocol = input("Enter the port (http or https): ").lower().strip()

	if domain == "" or user_protocol == "":
		print("Both field are required.")
		continue

	if user_protocol in protocols:
		print("="*30)
		print("Generated endpoints are given below:")
		for i in endpoints:
			print(f"{user_protocol}://{domain}/{i}")
		print("="*30)
	else:
		print("Invalid Protocol. Correct protocol (http or https).")
		continue

	break



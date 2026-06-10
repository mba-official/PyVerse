#!/usr/bin/env python3

# Welcome note
def banner():
	print(f"{"="*5} Unique Target Collector {"="*5}")


# Check for any error in user input
def check_error(domain):
	if domain == "":
		raise TypeError("Domain is requried.")


# Ask input from user
def get_domain():

	targets = set()
	while True:
		domain = input("(Press: 'Q for Quit, S for Show Domains')\nEnter the domain: ")
		domain = domain.lower().strip()
		try:
			if domain == "q":
				print("Program exist successfully.")
				break
			if domain == "s":
				count = 1
				print(f"{"="*5} Saved Domains {"="*5}")
				for i in targets:
					print(f"{count}: {i}")
					count += 1
			check_error(domain)
			if len(domain) > 4:
				targets.add(domain)
				print("Domain added successfully.")

		except Exception as e:
			print("Error:",e)
			continue

banner()
get_domain()

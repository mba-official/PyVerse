#!/usr/bin/env python3

from datetime import datetime # Import datetime for local date and time
import time # Import time for sleep

# Sample Data for Testing
database = {
	"testing.com" : {"ip" : "8.8.8.8", "status" : "Allow"},
	"example.com" : {"ip" : "1.1.1.1", "status" : "Allow"},
	"abc.com" : {"ip" : "8.8.4.4", "status" : "Block"},
	"xyz.com" : {"ip" : "1.1.0.0", "status" : "Block"},
	"test.com" : {"ip" : "149.122.112.112", "status" : "Allow"},
	"dfg.com" : {"ip" : "208.67.222.222", "status" : "Allow"},
	"abcd.com" : {"ip" : "208.67.220.22", "status" : "Block"},
	"jklm.com" : {"ip" : "94.140.14.14", "status" : "Allow"},
	"bcds.com" : {"ip" : "152.175.168.120", "status" : "Block"},
	"last.com" : {"ip" : "155.120.182.140", "status" : "Allow"},
}

# Ask for domain from user and strip the input
domain = input("Enter the domain: ").strip()

# Banner function to print welcome note
def banner():
	print(f"{"="*5} Welcome to Firewall Simulator {"="*5}")

# End function to print ending note
def ending():
	time_now = datetime.now()
	print(f"Program end on {time_now}\nThanks for using.")

# Function to check if there is an error in user input
def error(domain):
	if domain.isdigit():
		raise TypeError("Invalid domain.")

	if domain == "":
		raise ValueError("Domain name is required.")

	if "." not in domain:
		raise ValueError("Invalid domain.")
	return True

# Function to search user input domain in sample data and print result based on searching
def search(domain):
	try: 
		error(domain)
	except Exception as e:
	    print("Error:", e)
	    return None

	domain = domain.lower() #Auto lowercase user input, incase user enter Uppercase domain

	# Check the input domain if exist in sample data database.
	if domain in database:
		return database[domain]
	return None


# Print the result of
def output():
	result = search(domain)
	if result is None:
		return
	else:
		print("Searching...")
		time.sleep(2)
		if result:
			print(f"The IP Address of {domain} is: {result["ip"]}\nThe Status of This IP Address is {result["status"]}.")
		else:
			print("Domain not found.")


banner()
output()
ending()
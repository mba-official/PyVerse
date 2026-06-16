#!/usr/bin/env python3


import socket
import datetime

def check_connection():

	sock = socket.socket()

	while True:
		domain = input("Enter the domain: ")

		port = int(input("Enter the Port Number: "))

		if domain == "":
			print("Domain is required.")
			continue

		if port == "":
			print("Port is required.")
			continue


		try:
			start = datetime.datetime.now()
			sock.connect((domain, port))
			print("[+] Connection Succcessful")
			print(f"[+] Port {port} is opened.")
			end = datetime.datetime.now()
			print(f"Start Time: {start} --- End Time: {end}")
		except Exception as e:
			print("Error:",e)
			print(f"Port {port} is closed.")

		sock.close()

		break

check_connection()








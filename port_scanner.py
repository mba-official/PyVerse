#!/usr/bin/env python3

import socket
from datetime import datetime

target = input("Enter the IP address: ")

def port_scan(target):

	try:
		ip = socket.gethostbyname(target)

		print(f"Searching the target {ip}")
		print("Time Started:",datetime.now())


		for port in range(20, 500):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(1)

			result = sock.connect_ex((ip, port))

			if result == 0:
				print(f"Port Open: {port}")

			sock.close()

		print("Scan Completed Successfully.")
		print("Time End:",datetime.now())

	except socket.gaierror:
		print("Hostname could not resolved.")

	except socket.error:
		print("Could not connect to server.")

	except Exception as e:
		print("Error:",e)

port_scan(target)


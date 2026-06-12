#!/usr/bin/env python3

import requests

from pathlib import Path


def banner():
	print(f"{"="*5}> Alive Host Checker <{"="*5}")

# banner()

def modes():
	mode = input(f"{"-"*3}> Available Modes\n1. Press 1 to add domain you want to store in file.\n2. Press 2 to check domain already saved in file.\n3. Press 3 for exit program.\nPlease select mode: ")

	if mode == "":
		print("You did not select any mode. Program exit.")
	if mode == "1":
		return "1"

	if mode == "2":
		return "2"

	if mode == "3":
		return "3"


def add_domain():

	file_to_save = input("Enter the filename in which you want to save your domains: ").lower().strip()
	if not file_to_save.endswith(".txt"):
		correct_file_name = file_to_save+".txt"
		file_path = Path(correct_file_name)
		if file_path.exists():
			print(f"File {correct_file_name} already exist. You data will saved in existing file.")
		else:
			print(f"File {correct_file_name} created successfully.")

		while True:
			domain = input("Enter the domain you want to add: ").lower().strip()

			if domain == "":
				print("You did not enter domain. Domain is required.")
				continue

			if len(domain) <= 1:
				if domain == "0":
					print("You enter 0. Back to modes.")
					return redirect()

			if "." not in domain:
				print("Domain is Invalid. Try again.")
				continue

			if not domain.startswith(("http", "https")):
				correct_domain = "https://"+domain

			with open(correct_file_name, "a") as file:
				file.write(correct_domain+"\n")
			print("Domain added successfully. Press 0 to back on modes.")
			continue



def check_alive():

		choose_file = input("Enter filename which you want to check status: ")

		if choose_file == "":
			print("You did not enter filename. Program back to modes.")

		if len(choose_file) <= 1:
			if choose_file == "0":
				print("You enter 0. Program back to modes.")
				return modes()

		if not choose_file.endswith(".txt"):
			selected_file = choose_file+".txt"

		with open(selected_file, "r") as file:
			for url in file:
				correct_url = url.strip()
				if not correct_url:
					continue
				try:
					response = requests.get(correct_url)
					print(f"URL: {response.url}\nStatus Code: {response.status_code}")
					print("-"*10)
				except:
					print(f"Error: {correct_url} is not correct.")
					print("-"*10)
			print("Status checked successfully. Program back to modes.")
		return redirect()



def redirect():
	mode = modes()

	if mode == "1":
		print(f"{"-"*3}> Welcome, You select mode 1 Add domain in file. Press 0 to back on modes.")
		add_domain()


	if mode == "2":
		print(f"{"-"*3}> Welcome, You select mode 2 Check Alive domain from saved file. Press 0 to back on modes.")
		check_alive()

	if mode == "3":
		print("You enter 3. Program exit.")
		return


banner()

redirect()



#!/usr/bin/env python3


print("="*5,"Port Risk Checker", "="*5)

ports = {
	20: "Service: FTP Data\nPurpose: File transfer data channel",
	21: "Service: FTP Control\nPurpose: File transfer commands/authentication",
	22: "Service: SSH\nPurpose: Secure remote login and management",
	23: "Service: Telnet\nPurpose: Un-secure remote terminal access",
	25: "Service: SMTP\nPurpose: Sending email between servers",
	53: "Service: DNS\nPurpose: Domain name resolution",
	80: "Service: HTTP\nPurpose: Un-Secure Web Service",
	110: "Service: POP3\nPurpose: Receiving emails from server",
	143: "Service: IMAP\nPurpose: Email access and synchronization",
	443: "Service: HTTPS\nPurpose: Secure encrypted web service"
}

while True:
	user_raw_input = (input("Enter Port Number (or press q for Quit): "))

	try:
		if user_raw_input == "q":
			print("Program Exit Successfully")
			break

		user_input = int(user_raw_input)


	except ValueError:
		print(f"You Enter {user_raw_input}, which is not correct port.")
		continue

	if user_input in ports:
		print(f"Port Match Found: {user_input}\n{ports[user_input]}\n" + "-"*30)
	else:
		print("Port not found in local database.")
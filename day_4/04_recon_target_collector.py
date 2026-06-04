#!/usr/bin/env python3

print("Welcome to Recon Target Collector.\nCollect Your Targeted domain in a clean list.\n", end="="*30 + "\n")


targets = []

while True:

	user_target = input("Enter Your Target: ").lower().strip()

	if user_target == "":
		print("Target cannot be empty. Write domain.")
		continue

	targets.append(user_target)

	ask = input("Wanna add more targets (Y or N): ").lower()
	if ask.lower() != "y":
		break

print("="*30 + "\nYour target list.")

count = 1
for i in targets:
	print(f"{count}. {i}")
	count += 1
print("="*30)
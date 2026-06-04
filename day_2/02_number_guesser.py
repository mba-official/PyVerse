#!/usr/bin/env python3

secret = 6

guess_number = int(input("Guess the secret number: "))

if guess_number > secret:
	print(f"Guess {guess_number} is too high.")
elif guess_number < secret:
	print(f"Guess {guess_number} is too small.")
else:
	print(f"Guess {guess_number} is equal to secret {secret}.")
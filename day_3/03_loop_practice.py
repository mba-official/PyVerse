#!/usr/bin/env python3


# Infinite Loop
# while True:
# 	print("Noooo!")


# Mini game
counter = 1

where = input("Where you want to go? Left or Right: ")
while where == "right":
	where = input("Where you want to go? Left or Right: ")
	counter += 1

	if counter % 2 == 0:
		print("Sad!")

print("You go out.")



# For Loop
# mysum = 0
# start = 3
# end = 5

# for i in range(start, end+1):
# 	mysum += i
# print(mysum)

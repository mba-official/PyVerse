#!/usr/bin/env python3


import subprocess


target = input("Enter Target: ")

host = subprocess.run(f"host {target}", shell=True, capture_output=True, text=True)

nslookup = subprocess.run(f"nslookup {target}", shell=True, capture_output=True, text=True)

dig = subprocess.run(f"dig {target}", shell=True, capture_output=True, text=True)


print(f"{"= "*5} HOST {" ="*5}")
print(host.stdout)
print(f"{"-"*20}\n")

print(f"{"= "*5} NSLOOKUP {" ="*5}")
print(nslookup.stdout)
print(f"{"-"*20}\n")

print(f"{"= "*5} DIG {" ="*5}")
print(dig.stdout)
print(f"{"-"*20}\n")


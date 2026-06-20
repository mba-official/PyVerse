#!/usr/bin/env python3

import subprocess

target = input("Enter Target: ")

host_output = subprocess.run(f"host {target} | grep address", shell=True, capture_output=True, text=True)

get_ip = subprocess.run(f"host {target} | grep 'has address' | awk '{{print $4}}'", shell=True, capture_output=True, text=True)

print(f"{"= "*5} HOST OUTPUT {" ="*5}")
print(host_output.stdout)
print(f"{"-"*20}\n")

print(f"{"= "*5} GET IP ONLY {" ="*5}")
print(get_ip.stdout)
print(f"{"-"*20}\n")
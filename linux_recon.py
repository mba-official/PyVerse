#!/usr/bin/env python3
# import subprocess
import subprocess

target = input("Enter Target: ")

print(f"{"="*4} PING {"="*4}")
subprocess.run(f"ping -c 2 {target}", shell=True)
print(f"{"-"*10}\n")

print(f"{"="*4} HOST {"="*4}")
subprocess.run(f"host {target}", shell=True)
print(f"{"-"*10}\n")

print(f"{"="*4} WHOIS {"="*4}")
subprocess.run(f"whois {target}", shell=True)
print(f"{"-"*10}\n")

print(f"{"="*4} NSLOOKUP {"="*4}")
subprocess.run(f"nslookup {target}", shell=True)
print(f"{"-"*10}\n")

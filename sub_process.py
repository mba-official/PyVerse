#!/usr/bin/env python3

import subprocess


text = input("Enter the text: ")
file_name = input("Enter the filename: ")

subprocess.run(["echo", ">", text, file_name])


#!/usr/bin/env python3

import requests

response = requests.get("http://itsbilal.vercel.app/")

# this will print response
print(response)
print (type(response))

# this will print url
print(response.url)

# this will print status code of website
print(response.status_code)

# this will print header of the website
print(response.headers)

# this will print the entire body text of the website
print(response.text)

# this will print cookies of website
print(response.cookies)

# this will print json data of website
print(response.json())

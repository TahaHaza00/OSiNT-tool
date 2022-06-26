# IF NOT SUBSCRIBED
# This file will be unavailable for use.
# You must be subscribed to use this file.
# If you are not subscribed, please contact the owner of this file.
# If you are subscribed, please continue to use this file.

import requests

url = "https://breachdirectory.p.rapidapi.com/"

Email = input("Enter user's email: ")

querystring = {"func":"auto","term":"{Email}"}

headers = {
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "WEBSITE HOST (in this case it will be https://breachdirectory.p.rapidapi.com/)",
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# Latency
# 2,692ms

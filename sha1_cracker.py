#!/usr/bin/python3
from urllib.request import urlopen
import hashlib

hashsha1 = input("Enter your hash: \n")
wordlisturl = input("Enter your wordlist's url:\n ")
allw = str(urlopen(wordlisturl).read(), 'utf-8')

for crack in allw.split('\n'):
    hashcrack = hashlib.sha1(bytes(crack, 'utf-8')).hexdigest()
    if hashcrack == hashsha1:
        print("Password Found --> ", str(crack))
        quit()
    elif hashcrack != hashsha1:
        print("Password crack of --> ",str(crack), " not found")
print("Please choose another list and try again.")

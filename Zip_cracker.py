#!/usr/bin/python3
import zipfile
import colorama
from colorama import Fore, Back, Style
from threading import Thread


print("Password-protected zip file cracker..")
def zip_cracker(zipsec, password):
        try:
                 password = bytes(password.encode('utf-8'))
                 zipsec.extractall(pwd=password)
                 print(Fore.GREEN + "[*Password Found: " , str(password))
        except:
                pass

def Main():
        zipname = input("Name of protected zip: ")
        pname = input("Name of password file : ")
        if (zipname == None) | (pname == None):
             print(Fore.RED + "Incorrect File name!")
             exit(0)
        else:
            pass

        zipsec = zipfile.ZipFile(zipname)
        passFile = open(pname)

        for line in passFile.readlines():
            password = line.strip('\n')
            thr = Thread(target=zip_cracker, args=(zipsec, password))
            thr.start()

if __name__ == '__main__':
         Main()

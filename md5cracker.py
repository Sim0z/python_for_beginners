import sys
import hashlib
import colorama
from colorama import Fore, Back, Style


def md5cracker():
    #print(Fore.GREEN + "MD5 hashes cracked!")
    md5cracker = hashlib.md5()
    print("")
    hash_file = input("Hashes File: ")
    wordlist = input("Wordlist: ")
    try:
        hashdocument = open(hash_file, "r")
    except IOError:
        print("Wrong File name")
        input()
        sys.exit()
    else:
        crack = hashdocument.readline()
        crack = crack.replace("\n",(""))

    try:
        wordlistfile = open(wordlist, "r")
    except IOError:
        print("Wrong File name")
        input()
        sys.exit()

    else:
        pass
        for line in wordlistfile:
            md5cracker = hashlib.md5()
            line = line.replace("\n", (""))
            md5cracker.update(line.encode('utf-8'))
            word_hash = md5cracker.hexdigest()
            if word_hash == crack:
                print("")
                print(Fore.BLUE + "Great cracked!" , line)
                sys.exit()
            else:
                print("Hash not found !")
                sys.exit()
print("MD5 cracker"), md5cracker()

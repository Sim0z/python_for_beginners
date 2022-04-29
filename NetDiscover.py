#!/usr/bin/python3

#import the needed modules
import sh
from colorama import Fore, Back, Style

for i in range(1,254):
    target = "192.168.0."+str(i)

    try:
        sh.ping(target, "-c 1",_out="/dev/null")
        print(Fore.GREEN + "Host " + target + " is live")
    except sh.ErrorReturnCode_1:
        print(Fore.RED + "Host " + target + " is Down")


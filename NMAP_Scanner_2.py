#!/usr/bin/python3

# Import modules
import nmap
from colorama import Fore, Back, Style
import time
from time import sleep

#Variables
scanner = nmap.PortScanner()
ip_address = input("Enter Target Address: ")
port_range = input("Enter Port Range: ")
response = input("""\nSelect Scan Method:
                 1) SYN Scan
                 2) UDP Scan\n""")
print("Scan ",response," is in progress")

#Core Code
from tqdm import *
for i in tqdm(range(4)):
    time.sleep(1)

if response == '1':
    scanner.scan(ip_address,port_range, '-vvv -sT -T4')
    print(Fore.RED + 'Info: ', scanner.scaninfo())
    print("IP status: ", scanner[ip_address].state())
    for protocol in scanner[ip_address].all_protocols():
        print('Protocol: {}'.format(protocol))
        lport = scanner[ip_address][protocol].keys()
        for port_range in lport:
            print(Fore.GREEN + 'port: {}\tstate: {}'.format(port_range,scanner[ip_address][protocol][port_range]['state']))
else:
    scanner.scan(ip_address,port_range, '-vvv -sU -T4')
    print(Fore.RED + 'Info: ', scanner.scaninfo())
    print("IP status: ", scanner[ip_address].state())
    for protocol in scanner[ip_address].all_protocols():
        print('Protocol: {}'.format(protocol))
        lport = scanner[ip_address][protocol].keys()
        for port_range in lport:
            print(Fore.GREEN + 'port: {}\tstate: {}'.format(port_range,scanner[ip_address][protocol][port_range]['state']))






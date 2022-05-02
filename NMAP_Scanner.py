#!/usr/bin/python3

import nmap

print("Usage: \n(Enter Target Address:x.x.x.x) \n(Enter Port Range:20-100)")
print("-" *100)

address = input("Enter Target Address: ")
port_range = input("Enter Port Range: ")
portt = nmap.PortScanner()
portt.scan(address,port_range)
print(portt.command_line())

for host in portt.all_hosts():
    print("Scanning is in progress ..")
    print("Target Host : {} ({})".format(host, portt[host].hostname()))
    print("State: {}".format(portt[host].state()))
    for protocol in portt[host].all_protocols():
        print("Protocol: {}".format(protocol))

        lport = portt[host][protocol].keys()
        for port in lport:
            print('Port : {}\tstate: {}'.format(port,portt[host][protocol][port]['state']))

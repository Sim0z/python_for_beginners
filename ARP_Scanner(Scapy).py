#!/usr/bin/python3
from telnetlib import IP
from colorama import Fore, Back, Style
from scapy.all import *
from scapy.layers.l2 import Ether, ARP

ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.0.0/24"),timeout=2)

MM = (Fore.CYAN + "MAC: %Ether.src% ")
IP = (Fore.GREEN + "IP: %ARP.psrc% ")

ans.summary(lambda s_r: s_r[1].sprintf(Fore.RED + "Live Hosts: "+ MM + IP))

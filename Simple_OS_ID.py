#!/usr/bin/python3

from telnetlib import IP

from scapy.all import *
from scapy.layers.inet import ICMP

result = input("Enter target IP: ")

target = IP()
ping = ICMP()
target.dst = result
reply = sr1(target/ping)

if reply.ttl < 66:
    os = 'not windows'
else:
    os = 'windows'
print("Targeted system is " + os)

#!/usr/bin/python3
import sys
from telnetlib import IP

from pexpect import TIMEOUT
from scapy.all import *
from scapy.layers.inet import ICMP

TIMEOUT = 2
for ip in range(1,254):
    packet = IP(dst="192.168.0." + str(ip), ttl=20)/ICMP()
    reply = sr1(packet, timeout=TIMEOUT)
    if not (reply is None):
        print(reply.dst, "is UP")
    else:
        print(packet[IP].dst, "is DOWM")


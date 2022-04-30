#!/usr/bin/python3

#import the needed modules
import dns.resolver
from colorama import Fore, Back, Style

#Defining Variables
ans = input("Enter Domain Name: ")
#Answers
answer1 = dns.resolver.resolve(ans, 'A')
answer2 = dns.resolver.resolve(ans,'AAAA')
answer3 = dns.resolver.resolve(ans,'MX')
answer4 = dns.resolver.resolve(ans,'NS')

#Core of the code
for rdata in answer1:
    print("A record is " + str(rdata))
for rdata in answer2:
    print("AAAA record is " + str(rdata))
for rdata in answer3:
    print("MX record is " + str(rdata))
for rdata in answer4:
    print("NS record is " + str(rdata))

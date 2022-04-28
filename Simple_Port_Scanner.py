#!/usr/bin/python3

#import the needed
import socket
import threading

#define variables
target = input("Enter the target IP Address: ")
i = 1
print("Scan started..")
#define the scanning function
def pscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(.5)
    try:
        scan = s.connect((target, port))
        print('Port ',port,' is open')
        scan.close()
    except:
        pass

for x in range(1,1000):
    treadd = threading.Thread(target=pscan,kwargs={'port':i})
    i += 1
    treadd.start()

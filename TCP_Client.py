#!/usr/bin/path

import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 1234

c.connect((host, port))

msg = c.recv(1024)

c.close()

print(msg.decode('ascii'))

#!/usr/bin/python

import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 1234

server.bind((host,port))

##Set the queue of the requests up to 5
server.listen(5)
while True:
    clientsock, addr = server.accept()
    print("A Connection received from : %s" %str(addr))

    msg = 'Connect Back!' + "\r\n"
    clientsock.send(msg.encode('ascii'))
    clientsock.close()


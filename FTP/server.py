from socket import *
import sys
import os
import threading
import time

def send(sock,filename):
    with open(filename, 'r') as file:
        data = file.read()
        sock.send(data.encode('utf-8'))

def receive(sock):
    data=sock.recv(1024)
    req_data=data.decode('utf-8')
    send(sock,req_data)

serv_sock=socket(AF_INET,SOCK_STREAM)
serv_sock.bind( ('',int(sys.argv[1])))
serv_sock.listen();

connect_sock, addr = serv_sock.accept()
print('\nTCP client connect.')

while True:
    receive(connect_sock)

from socket import *
import threading
import time
import sys

def send(sock):
    while True:
        data=input(">>")
        sock.send(data.encode('utf-8'))

def receive(sock):
    while True:
        data=sock.recv(1024)
        print('상대방 :',data.decode('utf-8'))

clnt_sock = socket(AF_INET, SOCK_STREAM)
clnt_sock.connect(('127.0.0.1',int(sys.argv[1])))

sender = threading.Thread(target=send, args=(clnt_sock,))
receiver = threading.Thread(target=receive, args=(clnt_sock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass

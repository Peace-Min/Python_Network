from socket import *
import sys
import threading
import time
cnt=[]
recv=[]
i=0
def send():
    while True:
        mode=int(input("1.전체 메세지 전송 2.귓속말 3.종료"))
        if mode==1:
            broad_data=input(">>")
            for j in range(i):
                cnt[j].send(broad_data.encode('utf-8'))

        elif mode==2:
            data=input(">>")
            who=int(input("몇 번째 클라이언트한테 전송할 것?"))
            cnt[who].send(data.encode('utf-8'))

        elif mode==3:
            for j in range(i):
                cnt[j].close()
            serv_sock.close()
            sys.exit()
            break
            
        else:
            print("잘못된 입력")
            mode=int(input("1.전체 메세지 전송 2.귓속말 3.종료"))

def receive(sock):
    while True:
        data=sock.recv(1024)
        print("\nclnt[{}] ".format(i),data.decode('utf-8'))

def serv(sock, i):
    recv.append(threading.Thread(target=receive, args=(sock,)))
    recv[i].start()
        
serv_sock=socket(AF_INET,SOCK_STREAM)
serv_sock.bind( ('',int(sys.argv[1])))
serv_sock.listen();

sender=threading.Thread(target=send, args=())
sender.start()
while True:
    connect_sock, addr = serv_sock.accept()
    cnt.append(connect_sock)
    print('\nTCP client {} connect.'.format(i))
    serv_t=threading.Thread(target=serv, args=(connect_sock,i))
    serv_t.start()
    i+=1


# Python_Network
> 간단한 네트워크 프로그래밍을 파이썬으로 구현해보고자 만들었습니다.
---
***구현 목록***
1. Multi-chatting (6.23 완료) 
2. FTP (6-25 완료)
  --- 
# 1. Multi-chatting
* Socket을 통한 Multi-Chatting입니다.</br></br>
* Thread를 통해 동시에 여러 Client가 접속할 수 있습니다.</br></br>
* Server는 Send Thread 생성, Client는 개별의 Receive Thread를 통해 메세지 통신
</br>
**옵션**</br>
**1. 전체전송** **2. 귓속말**

* *  **1.전체전송**: 서버와 연결된 Client의 소켓 정보를 cnt[]배열에</br> 저장한 후 순차적으로 counting하여 배열에 저장하였습니다.</br> 그 후 cnt[]배열에 저장 된 전체 client들에게 broadcast</br>하는 방식으로 구현하였습니다.

* * **2.귓속말:** cnt[]배열에 저장 된 socket 정보를 입력하여 </br>해당 client에게만 메세지를 전송하도록 구현하였습니다.

># 구현 사진
![Alt text](image-6.png)
![Alt text](image-7.png)
![Alt text](image-8.png)

**후기**
* 다른 Multi-Chatting 구현은 Server에서 Client의 메세지를 받자마자</br> 연결 된 모든 Client한테 메세지를 **Broadcast**하는 예제를 많이 보았습니다.</br></br>      
* 제가 구현한 방식은 Client한테 메세지를 Server에서 저장하고 필요한 메세지만 </br>**Broadcast**, **Unicast** 전송 방식을 정하는 방식으로 구현하였습니다.

---
# 2. FTP

>python은 ftplib라는 표준 라이브러리가 존재하여 이 라이브러리를 </br>사용하면 매우 간단하게 구현가능합니다. 하지만 저는 실질적으로 FTP보단 FTP과정을 python의 socket과정을 </br>거쳐서 파일 입출력을 사용해보는 것을 목적을 두었기 때문에 ftplib 라이브러리는 사용하지 않았습니다. </br>또한 다양한 FTP 예제는 server의 처리에서 다양한 시스템 콜을 처리하지만 </br>이번 python에서 구현한 ftp는 매우 협소하게 원하는 파일 이름을 받고 </br>파일 이름을 열어서 내용을 보내는 식으로 아주 간단하게 구현하였습니다.

**동작**
* Server는 Client의 요청만을 기다리고 그에 대응하는 응답을 해주기 때문에 Server에서는 Thread를 사용하지 않았습니다.</br> Client는 주기적으로 Server에게 요청도하고 응답도 받아야하기 때문에 send, receive에 해당하는 Thread를 생성하였습니다.

># 구현 사진
![Alt text](image-9.png)
**후기**
* 이번 FTP는  매우 협소하게 원하는 파일 이름을 받고 파일 이름을 열어서 </br>내용을 보내는 식으로 아주 간단하게 구현에 목적을 두었기에 내가봐도 </br>부끄러운 작품이다. </br>그렇지만 제대로 된 FTP는 C언어를 사용해서 제대로 작성할 예정이다.

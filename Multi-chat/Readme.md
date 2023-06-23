소켓을 통한 Multi-Chatting입니다. Thread를 통해 동시에 여러 Client가 접속할 수 있습니다.
Server에는 Send를 전체적으로 다루고 있는 Thread 하나를 생성하였고,
Client마다 Receive를 할 수 있는 개별의 Thread를 통해서 메세지 전송과 수신을 동시에 할 수 있게 하였습니다.

Send 옵션은 1. 전체전송 2. 귓속말 3. 종료입니다.
1. 전체전송은 서버와 연결된 Client의 소켓 정보를 cnt[]배열에 저장한 후 순차적으로 counting하여 배열에 저장하였습니다.
그 후 cnt[]배열에 저장 된 전체 client들에게 broadcast하는 방식으로 구현하였습니다.

2. 귓속말은 cnt[]배열에 저장 된 socket 정보를 입력하여 해당 client에게만 메세지를 전송하도록 구현하였습니다.

python은 ftplib라는 표준 라이브러리가 존재하여 이 라이브러리를 사용하면 매우 간단하게 구현가능합니다.
하지만 저는 실질적으로 ftp보단 ftp과정을 python의 socket과정을 거쳐서 파일 입출력을 사용해보는 것을 목적을 두었기 때문에 ftplib 라이브러리는 사용하지 않았습니다.
또한 다양한 ftp 예제는 server의 처리에서 다양한 시스템 콜을 처리하지만 이번 python에서 구현한 ftp는 매우 협소하게 원하는 파일 이름을 받고 그 파일 이름을 열어서
내용을 보내는 식으로 아주 간단하게 구현하였습니다.

Server는 Client의 요청만을 기다리고 그에 대응하는 응답을 해주기 때문에 Server에서는 Thread를 사용하지 않았습니다.
Client는 주기적으로 Server에게 요청도하고 응답도 받아야하기 때문에 send, receive에 해당하는 Thread를 생성하였습니다.

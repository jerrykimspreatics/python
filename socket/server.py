import socket

# 소켓 객체 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓 정보세팅(튜플)
server_address = ('localhost', 9999)
print('Start up on {} port {}'.format(*server_address))

# 소켓 정보 바인딩
server_socket.bind(server_address)

# 소켓 가동
server_socket.listen()

while True:
    print('accept wait')

    # 클라이언트 접속 대기
    client_socket, client_address = server_socket.accept()

    try:
        # 클라이언트가 보낸 데이터 수령(1024byte)
        data = client_socket.recv(1024)
        # 문자열 치환
        data = data.decode()

    except Exception as err:  # 예외 발생 시
        # 클라이언트 소켓 연결 끊기
        client_socket.close()
        break
    finally:  # 모든 작업이 종료
        client_socket.close()
        break
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9999)

# 서버 소켓에 접속
client_socket.connect(server_address)

while True:
    # try:
    data = input('')
    # 입력 값에 특정 문자 식별 시 소켓 종료
    if data == 'quit':
        break
    data = data.encode()
    client_socket.send(data)
    # except Exception as err:  # 예외 발생 시
    #     # 클라이언트 소켓 연결 끊기
    #     client_socket.close()
    #     break
    # finally:  # 모든 작업이 종료
    #     client_socket.close()
    #     break

client_socket.close()


def recv_message():
    message = client_socket.recv(1024)

    message = message.decode()

    # 스레드로 실행
# start_new_thread(recv_message, (client_socket,))
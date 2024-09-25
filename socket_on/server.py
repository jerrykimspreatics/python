import socket

print("1. 소켓 생성")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 9700))

server.listen()

client, addr = server.accept()

read_data = client.recv(1024)

print(f"수신: {read_data}")

client.close()
server.close()
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 9700))

client.sendall(bytes('Hello~ Server', 'utf-8'))

client.close()
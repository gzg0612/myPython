import socket

BUF_SIZE = 1024 
host = 'localhost'
port = 10010

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
client, address = server.accept()


while True:
    data = client.recv(BUF_SIZE)
    client.send(data)
    print(data.decode())

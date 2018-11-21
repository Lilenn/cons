import socket

sock = socket.socket(type=socket.SOCK_STREAM,family=socket.AF_INET)

sock.connect(('127.0.0.1',9000))

while True:
    msg = input('>>>>>: ')
    sock.send(msg.encode())
    server_msg = sock.recv(10240000)
    print(server_msg.decode('GBK'))
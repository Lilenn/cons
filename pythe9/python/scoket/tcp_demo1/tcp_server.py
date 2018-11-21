import socket

sock = socket.socket(type=socket.SOCK_STREAM)

sock.bind(('127.0.0.1',9003))

sock.listen()

client_sock,client_address = sock.accept()

# 循环的读写操作
while True:
    client_msg = client_sock.recv(1024)
    if client_msg == b'yang':
        client_sock.send('我知道了'.encode())
        continue
    print('这是从客户端接到的消息: ',client_msg.decode())
    client_sock.send('ffaf'.encode())

client_sock.close()
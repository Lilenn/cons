import socket

sock = socket.socket(type=socket.SOCK_STREAM,family=socket.AF_INET)

# 连接服务端
sock.connect(('127.0.0.1',9003))

while True:
    msg = input('请输入内容：')
    # 客户端向服务端发送消息
    sock.send(msg.encode())
    # 从服务端接收消息
    server_msg = sock.recv(1024)
    print('服务端发送来的消息',server_msg.decode())

sock.close()

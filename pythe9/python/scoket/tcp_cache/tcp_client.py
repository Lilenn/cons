import socket

# 1.初始化
sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

# 2.连接服务端
sock.connect(('127.0.0.1',9098))
# 3.发送接收消息
# 字符串前边加上B代表为byte类型，eg：b"hello"
# 因为流的传输类型为byte类型，所以要吧字符串转化为byte类型
while True:
    # sock.send(b'hello,world')
    msg= sock.recv(1024).decode('utf-8')
    print(msg)
    lenght = int(sock.recv(1024).decode('utf-8'))
    print(lenght)

    sock.send('recv_ready'.encode('utf-8'))

    server_msg = sock.recv(lenght)
    print(server_msg.decode('utf-8'))

    # 4.关闭连接
    sock.close()

import socket

# 初始化socket
sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

# 2.连接服务端

sock.connect(('127.0.0.1',9000))

# 3.给服务端发送消息
sock.send('我是一个tcp的client端'.encode())
# 接收服务端的消息
ret = sock.recv(1024)
print(ret.decode())
# 4.关闭socket连接

sock.close()
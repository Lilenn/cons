import socket

# 1.初始化
sock = socket.socket(type=socket.SOCK_DGRAM)

# 2.发送消息
sock.sendto('我是udp的客户端'.encode(),('127.0.0.1',9001))
# 接收服务端的消息
server_msg,address = sock.recvfrom(1024)
print(server_msg.decode())
sock.close()
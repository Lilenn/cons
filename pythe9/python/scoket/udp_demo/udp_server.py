import  socket

# 1.初始化socket 创建套接字

sock = socket.socket(type=socket.SOCK_DGRAM)

# 2.绑定本地ip和端口
sock.bind(('127.0.0.1',9001))

# 3.接收|发送消息
client_msg,client_addr = sock.recvfrom(1024)
print('这是接收客户端的消息',client_msg.decode())

# 给client 端发送消息
print(client_addr)
sock.sendto('我是udp的服务端'.encode(),client_addr)

# 4.关闭
sock.close()
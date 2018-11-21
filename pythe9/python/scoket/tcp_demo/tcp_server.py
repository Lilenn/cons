import socket

# 1.创建socket对象
# socket_stream tcp
# socket_dgram udp
sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
# 绑定本地的ip与端口
sock.bind(('127.0.0.1',9000))
# 3.监听
sock.listen()

# 接受 接收（客户端发来的请求，如果没有，就会以直阻塞）
print('acect start')
client_sock, client_addr =sock.accept()

print(client_addr)
# 5.接收和发送消息
ret = client_sock.recv(1024)
print(ret.decode())
# 发送消息到客户端
client_sock.send('我收到了你的消息'.encode())

# 6.关闭
client_sock.close()
sock.close()
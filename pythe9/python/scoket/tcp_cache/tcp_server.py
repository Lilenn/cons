import socket

# 1.初始化socket对象
sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 2.绑定
sock.bind(('127.0.0.1',9098))
# # 3.监听
sock.listen()
while True:
    # 4.接收客户端连接
    conn,(ip,port) = sock.accept()
    # 5.接收/发送消息
    conn.send('hello'.encode('utf-8'))
    data1 = conn.recv(1024)
    send_msg = 'hello,client! i am coming!'
    send_msg_length = len(send_msg)
    conn.send(str(send_msg_length).encode('utf-8'))

    # 接收客户端确认已经准备接收数据消息
    data_recv = conn.recv(1024).decode('utf-8')
    if data_recv == 'recv_ready':
        # 如果客户端已经准备好接收消息，那么就发送数据到客户端
        conn.send(send_msg.encode('utf-8'))
    # 6.关闭连接
    conn.close()
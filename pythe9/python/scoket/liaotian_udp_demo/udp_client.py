import socket

sock = socket.socket(type=socket.SOCK_DGRAM)

name_dict = {
    'egg':('192.168.52.226',9002),
    'aaa':('127.0.0.1',9002),
    'lili':('127.0.0.1',9002),
    'yang':('127.0.0.1',9002)
}

while True:
    client_msg = input('请输入聊天对象:')
    if client_msg == 'q':
        break
    address = name_dict.get(client_msg,('192.168.52.253',9002))
    sock.sendto(client_msg.encode(),address)

    server_msg,server_address = sock.recvfrom(1024)
    print('来自服务端的消息：',server_msg.decode())
sock.close()
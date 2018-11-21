import socket

sock = socket.socket(type=socket.SOCK_DGRAM)

sock.bind(('192.168.52.253',9002))

while True:
    client_msg, client_address = sock.recvfrom(1024)
    print('来自[{ip}:{port}]的一条信息: {msg}'.format(ip=client_address[0],
                                               port = client_address[1],
                                               msg = client_msg.decode()))
    back_msg = input('回复消息：')
    sock.sendto(back_msg.encode(),client_address)
import socket
import hmac
import hashlib

secret_key = b'haxi[%ben*que#akhe]pophasmueny'

def conn_auth(conn):
    '''
    验证客户端到服务器的连接
    :param conn:
    :return:
    '''
    msg = conn.recv(32)
    h = hmac.new(secret_key,msg,hashlib.sha1)
    digest = h.digest()
    conn.sendall(digest)

def client_handel(ip_port,bufsize=1024):
    '''
    客户端入口
    :param ip_port:
    :param bufsize:
    :return:
    '''
    sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    sock.connect(ip_port)

    conn_auth(sock)

    while True :
        data = input('请输入要给服务端的数据: ')
        sock.sendall(data.encode('utf-8'))
    sock.close()

if __name__ == '__main__':
    ip_port = ('127.0.0.1',9097)
    bufsize = 1024

    client_handel(ip_port,bufsize)
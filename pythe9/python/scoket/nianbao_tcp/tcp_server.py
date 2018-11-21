import socket
import subprocess

sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 绑定ip与端口
sock.bind(('127.0.0.1',9000))

# 监听
sock.listen()

while True:
    conn,addr = sock.accept()
    print('客户端：',addr)
    while True:
        cmd = conn.recv(1024)
        res = subprocess.Popen(cmd.decode(),shell=True,stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        #标准输出错误
        stderr = res.stdout.read()
        # 标准输出的结果
        stdout = res.stdout.read()
        conn.send(stderr)
        conn.send(stdout)
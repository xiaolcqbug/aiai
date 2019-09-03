from socket import *

ip = 'localhost'
port = 46283
add = (ip, port)
buf_size = 1024

tcp_CliSock = socket(AF_INET, SOCK_STREAM)
tcp_CliSock.connect(add)

while 1:
    msg = input('客户端请输入:----->')
    tcp_CliSock.send(msg.encode("utf8"))

    res = tcp_CliSock.recv(buf_size)
    print('服务端传来的数据:-->', res.decode("utf8"))

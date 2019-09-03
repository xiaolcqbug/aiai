from socket import *
host = '127.0.0.1'
port = 3302
add = (host,port)
tcp_clisock= socket(AF_INET,SOCK_STREAM)
tcp_clisock.connect(add)
while True:
    data = input('客户端输入:')
    if not data:
        break
    tcp_clisock.send(data.encode('utf-8'))
    data = tcp_clisock.recv(1024)
    print('接收到来自服务器的信息为:',data.decode('utf-8'))
tcp_clisock.close()
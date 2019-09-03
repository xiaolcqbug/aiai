from socket import *

ip = '192.168.1.27'
port = 8999
add = (ip, port)
busize = 1024
tcpclisock = socket(AF_INET, SOCK_STREAM)
tcpclisock.connect(add)
while 1:
    data = input('请输入需要发送的信息:')
    if not data:
        break
    tcpclisock.send(data.encode('utf-8'))
    data = tcpclisock.recv(busize)
    if not data:
        break
    print(data.decode('utf-8'))

tcpclisock.close()
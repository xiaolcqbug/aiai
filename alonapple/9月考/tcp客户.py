from socket import *

ip = '192.168.1.9'
port = 8888
add = (ip, port)
busize = 1024
tcpclisock = socket(AF_INET, SOCK_STREAM)
tcpclisock.connect(add)
data = input('请输入需要发送的信息:')
tcpclisock.send(data.encode('utf-8'))
data = tcpclisock.recv(busize)

tcpclisock.close()
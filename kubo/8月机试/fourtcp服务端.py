from socket import *

ip = '192.168.1.27'
port = 8999
address = (ip, port)
bufsize = 1024
tcpsevsock = socket(AF_INET, SOCK_STREAM)
tcpsevsock.bind(address)
tcpsevsock.listen(5)
print('等待客户端连接')
tcpsevsock, cliAddress = tcpsevsock.accept()
print('来自:', cliAddress, '的连接')
print('来自:', tcpsevsock, '的连接')
while 1:
    data = tcpsevsock.recv(bufsize)
    if not data:
        break
    data1 = data.decode('utf-8')
    tcpsevsock.send(('你的消息:'+data1).encode("utf-8"))
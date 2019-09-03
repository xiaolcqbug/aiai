from socket import *

ip = '192.168.1.27'
port = 8999
address = (ip, port)
bufsize = 1024
udpsevsock = socket(AF_INET, SOCK_DGRAM)
print('等待客户端连接')
while 1:
    xinxi = input('请输入:')
    if not xinxi:
        break
    udpsevsock.sendto(xinxi.encode('utf-8'), address)

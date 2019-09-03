
from socket import *

ip = '192.168.1.9'
port = 8880
address = (ip, port)
bufsize = 1024
udpsevsock = socket(AF_INET, SOCK_DGRAM)
print('已连接')
a = input('请输入:')
udpsevsock.sendto(a.encode('utf-8'), address)
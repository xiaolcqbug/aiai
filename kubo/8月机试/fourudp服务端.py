from socket import *

host = '192.168.1.27'
port = 8999
address = (host, port)
bufsize = 1024
udpsevsock = socket(AF_INET, SOCK_DGRAM)
udpsevsock.bind(address)
print('等待连接')
while 1:
    ipdz, addr = udpsevsock.recvfrom(bufsize)
    print("来自：%s 发送来的消息：%s" % (addr, ipdz.decode("utf-8")))

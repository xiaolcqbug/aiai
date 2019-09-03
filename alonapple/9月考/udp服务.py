


from socket import *

host = '192.168.1.9'
port = 8880
address = (host, port)
bufsize = 1024

udpsevsock = socket(AF_INET, SOCK_DGRAM)
udpsevsock.bind(address)
print('等待连接')
ipdz, addr = udpsevsock.recvfrom(bufsize)
print("%s 发送来的消息：%s" % (addr, ipdz.decode("utf-8")))



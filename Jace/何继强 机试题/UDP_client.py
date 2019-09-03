from socket import *
from threading import *


cip = 'localhost'
port = 8888
address = (cip,port)
size = 1024
udp_socket = socket(AF_INET,SOCK_DGRAM)

while True:
    mas = input('请输入:')
    if not mas:
        print('程序终止')
        break
    udp_socket.sendto(mas.encode('utf8'), address)


udp_socket.close()

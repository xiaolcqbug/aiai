from socket import *

ip = '127.0.0.1'
port = 2222
address = (ip,port)  # 接收方
bufsize = 1024

sever_socket = socket(AF_INET,SOCK_DGRAM)

while 1:

    masg = input('input:')
    masg1 = masg.encode('utf8')
    sever_socket.sendto(masg1,address)

sever_socket.close()

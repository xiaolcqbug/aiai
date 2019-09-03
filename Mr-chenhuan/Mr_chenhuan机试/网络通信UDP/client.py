from socket import *

ip = '127.0.0.1'
port = 2222
address = (ip,port)
bufsize = 1024

client_socket = socket(AF_INET,SOCK_DGRAM)
client_socket.bind(address)

while 1:
    recv_masg,address1 = client_socket.recvfrom(bufsize)
    print('{}发送来消息'.format(address1))
    print(recv_masg.decode('utf8'))


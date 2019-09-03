from socket import *

ip='127.0.0.1'
port=6767
address=(ip,port)

tcp_socket=socket(AF_INET,SOCK_STREAM)
tcp_socket.connect(address)

while 1:
    mag=input('请输入:')
    tcp_socket.send(mag.encode('utf8'))
    continue
tcp_socket.close()
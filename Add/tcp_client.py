from socket import *


ip='localhost'
port=8888
address=(ip,port)
tcp_socket=socket(AF_INET,SOCK_STREAM)
tcp_socket.connect(address)

while 1:
    msg=input('<发送:>')
    tcp_socket.send(msg.encode('utf8'))
    continue
tcp_socket.close()


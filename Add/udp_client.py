from socket import *
ip='localhost'
port=7777
address=ip,port
udp_socket=socket(AF_INET,SOCK_DGRAM)
udp_socket.connect(address)

while 1:
    msg=input('<发送:')
    udp_socket.sendto(msg.encode('utf8'),address)
    continue
udp_socket.close()
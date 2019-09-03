from socket import *

ip='127.0.0.1'
port=4406
address=(ip,port)

udp_send_socket=socket(AF_INET,SOCK_DGRAM)

while True:
    msg=input('请输入:')

    udp_send_socket.sendto(msg.encode('utf-8'),address)

udp_send_socket.close()
from socket import *
ip='127.0.0.1'
port=8090
address=(ip,port)
buf_size=1024

udp_socket=socket(AF_INET,SOCK_DGRAM)

while True:
    msg = input("...")
    if not msg:
        break
    udp_socket.sendto(msg.encode("utf-8"), address)
    print(udp_socket.recv(1024).decode('utf-8'))

udp_socket.close()


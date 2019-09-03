from socket import *

ip = '127.0.0.1'
port = 4321
address = (ip,port)
bufsize = 1024

client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(address)
while 1:
    send_masg = input('input:')
    send_masg1 = send_masg.encode('utf8')
    client_socket.send(send_masg1)
    recv_masg = client_socket.recv(bufsize)
    print(recv_masg.decode('utf8'))

client_socket.close()
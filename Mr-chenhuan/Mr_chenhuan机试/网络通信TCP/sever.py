from socket import *

ip = '127.0.0.1'
port = 4321
address = (ip,port)
bufsize = 1024

sever_socket = socket(AF_INET,SOCK_STREAM)
sever_socket.bind(address)
sever_socket.listen(10)

client_socket,address1 = sever_socket.accept()
print('from {} "s connect'.format(address1))
while 1:
    recv_masg = client_socket.recv(bufsize)
    recv_masg1 = recv_masg.decode('utf8')
    if recv_masg1 == 'over':
        print('服务器退出')
        break
    else:
        print(recv_masg1)
        send_masg = input('input:')
        client_socket.send(send_masg.encode('utf8'))
client_socket.close()
sever_socket.close()
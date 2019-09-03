from socket import *

ip = '127.0.0.1'
port = 54321
add = (ip, port)
buf_size = 1024

tcp_server_socket = socket(AF_INET, SOCK_STREAM)

tcp_server_socket.bind(add)

tcp_server_socket.listen(5)

print('*****等待客户端连接*****')

client_socket, client_add = tcp_server_socket.accept()

print('来自*{}*客户端的连接'.format(client_add))

data = client_socket.recv(buf_size)
data = data.decode('utf-8')
print('客户端传来数据>>> {}'.format(data))

tcp_server_socket.close()
client_socket.close()

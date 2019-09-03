from socket import *

ip = '127.0.0.1'
port = 54321
add = (ip, port)
buf_size = 1024

udp_server_socket = socket(AF_INET, SOCK_DGRAM)

udp_server_socket.bind(add)

print('*****等待客户端连接*****')

client_data, client_add = udp_server_socket.recvfrom(buf_size)
client_data = client_data.decode('utf-8')
print('收到来自*{}*客户端发来的信息\n>>>{}'.format(client_add, client_data))

udp_server_socket.close()

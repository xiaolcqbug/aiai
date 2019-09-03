from socket import *

ip = '127.0.0.1'
port = 54321
address = (ip, port)

udp_sever_socket = socket(AF_INET, SOCK_DGRAM)
udp_sever_socket.bind(address)

data, client_socket = udp_sever_socket.recvfrom(1024)
data = data.decode('utf8')
print('来自{}的消息:{}'.format(client_socket, data))
udp_sever_socket.close()
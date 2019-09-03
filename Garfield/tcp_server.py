from socket import *

ip = '127.0.0.1'
port = 54321
address = (ip, port)
buf_size = 1024

tcp_sever_socket = socket(AF_INET, SOCK_STREAM)
tcp_sever_socket.bind(address)
tcp_sever_socket.listen(5)

client_socket, client_address = tcp_sever_socket.accept()

data = client_socket.recv(buf_size)
data = data.decode('utf8')
print('来自{}的消息:{}'.format(client_address, data))
client_socket.close()
tcp_sever_socket.close()
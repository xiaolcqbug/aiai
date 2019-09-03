from socket import *

ip = '127.0.0.1'
port = 54321
address = (ip, port)

tcp_client_socket = socket(AF_INET, SOCK_STREAM)

tcp_client_socket.connect(address)

message = input('请输入:')
tcp_client_socket.send(message.encode('utf8'))
tcp_client_socket.close()
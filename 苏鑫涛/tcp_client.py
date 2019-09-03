from socket import *

ip = '127.0.0.1'
port = 54321
add = (ip, port)
buf_size = 1024

tcp_client_socket = socket(AF_INET, SOCK_STREAM)

tcp_client_socket.connect(add)

info = input('请输入:')
tcp_client_socket.send(info.encode('utf-8'))

tcp_client_socket.close()

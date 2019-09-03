from socket import *

ip = '127.0.0.1'
port = 54321
add = (ip, port)

udp_client_socket = socket(AF_INET, SOCK_DGRAM)

info = input('请输入:')

udp_client_socket.sendto(info.encode('utf-8'), add)

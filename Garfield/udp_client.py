from socket import *

ip = '127.0.0.1'
port = 54321
address = (ip, port)

udp_sever_socket = socket(AF_INET, SOCK_DGRAM)

message = input('请输入:')
message = message.encode('utf8')
udp_sever_socket.sendto(message, address)
udp_sever_socket.close()
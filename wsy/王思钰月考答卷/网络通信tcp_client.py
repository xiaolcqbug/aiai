from socket import *


ip = '192.168.1.24'
port = 4407
address = (ip, port)
buf_size = 1024

tcp_client_socket = socket(AF_INET, SOCK_STREAM)
tcp_client_socket.connect(address)

while True:
    msg = input('哆啦A梦发送消息:')
    tcp_client_socket.send(msg.encode('utf-8'))
    res = tcp_client_socket.recv(buf_size)
    res_str = res.decode('utf-8')
    print(res_str)


tcp_client_socket.close()

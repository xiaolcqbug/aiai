from socket import *

ip = '127.0.0.1'
port = 56442
address = (ip, port)
buf_size = 1024
tcp_client_socket = socket(AF_INET, SOCK_STREAM)
tcp_client_socket.connect(address)
while True:
    msg = input('请客户端输入:')
    tcp_client_socket.send(msg.encode('utf-8'))
    res = tcp_client_socket.recv(buf_size)
    res_str = res.decode('utf-8')
    print(res_str)
    if res_str == 'no':
        print('客户端执行退出中..')
        break

tcp_client_socket.close()
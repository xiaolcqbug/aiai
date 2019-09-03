from socket import *
import _ip

tcp_client_socket = socket(AF_INET, SOCK_STREAM)
port = 7789
address = (_ip.ip, port)
tcp_client_socket.connect(address)
while True:
    msg = input('请输入:')
    tcp_client_socket.send(msg.encode('utf-8'))
    res = tcp_client_socket.recv(1024)
    print(res.decode('utf-8'))
tcp_client_socket.close()

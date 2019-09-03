from socket import *
ip = "127.0.0.1"
port = 54321
address = (ip, port)
buf_size = 1024
tcp_client_socket = socket(AF_INET, SOCK_STREAM)
tcp_client_socket.connect(address)
while 1:
    msg = input("请输入：")
    tcp_client_socket.send(msg.encode("utf-8"))

#  网络通信   一收一发    tcp  /  udp  两种模式    (四个文件)
from socket import *
ip = "127.0.0.1"
port = 54666
address = (ip, port)
buf_size = 1024
tcp_server_socket = socket(AF_INET, SOCK_STREAM)
tcp_server_socket.bind(address)
tcp_server_socket.listen(5)
print("-----等待客户端的链接------")
client_socket, client_adress = tcp_server_socket.accept()
while 1:
    print("来自 %s 的链接。。" % str(client_adress))
    data = client_socket.recv(buf_size)
    data = data.decode("utf-8")
    print("客户端传来的数据：%s" % data)
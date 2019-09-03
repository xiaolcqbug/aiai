#  网络通信   一收一发    tcp  /  udp  两种模式    (四个文件)
from socket import *
ip = "localhost"
port = 4406
address = (ip, port)
buf_size = 1024
udp_recv_socket = socket(AF_INET, SOCK_DGRAM)
udp_recv_socket.bind(address)

while True:
    print("等待别人给我发送的数据。。")
    data, send_address = udp_recv_socket.recvfrom(buf_size)
    print("来自：%s 发送来的消息：%s" % (str(send_address), data.decode("utf-8")))
#  网络通信   一收一发    tcp  /  udp  两种模式    (四个文件)
from socket import *
ip = "localhost"
port = 4406
address = (ip, port)
udp_send_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input("请输入：")
    if not msg:
        print("结束发送方程序。。")
        break
    udp_send_socket.sendto(msg.encode("utf-8"), address)
udp_send_socket.close()
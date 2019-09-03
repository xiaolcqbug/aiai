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
    data, send_address=udp_send_socket.recvfrom(1024)
    print('接收到来自服务器端的数据{}'.format(data.decode('utf-8')))
udp_send_socket.close()

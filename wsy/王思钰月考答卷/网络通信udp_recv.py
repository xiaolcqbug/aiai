from socket import *

# 1.初始化信息
ip = "192.168.1.24"
port = 4406
address = (ip, port)
buf_size = 1024

udp_recv_socket = socket(AF_INET, SOCK_DGRAM)
udp_recv_socket.bind(address)

# 3.结束发送来的数据
while True:
    print("等待熊二发送消息...")
    data, send_address = udp_recv_socket.recvfrom(buf_size)
    print("来自：熊二%s 发送来的消息：%s" % (str(send_address), data.decode("utf-8")))
    str1 = input('熊大发送消息:')
    udp_recv_socket.sendto(str1.encode('utf-8'),send_address)
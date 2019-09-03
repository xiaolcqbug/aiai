from socket import *
ip = '127.0.0.1'
port = 6767
address = (ip, port)
buf_size = 1024
udp_recv_socket = socket(AF_INET, SOCK_DGRAM)
udp_recv_socket.bind(address)

while True:
    print("等待客户端发送数据--")
    data, send_address = udp_recv_socket.recvfrom(buf_size)
    print("来自：%s 发送来的消息：%s" % (str(send_address), data.decode("utf-8")))

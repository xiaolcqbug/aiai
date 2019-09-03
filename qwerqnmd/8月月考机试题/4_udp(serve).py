from socket import *
ip = "localhost"
port = 6636
address = (ip, port)
buf_size = 1024
udp_recv_socket = socket(AF_INET, SOCK_DGRAM)
udp_recv_socket.bind(address)


while True:
    print("等待信息.........")
    data, send_address = udp_recv_socket.recvfrom(buf_size)
    print("来自：%s 发送来的消息：%s" % (str(send_address), data.decode("utf-8")))

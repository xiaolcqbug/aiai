from socket import *
ip = "localhost"
port = 4406
address = (ip, port)
buf_size = 1024
udp_recv_socket = socket(AF_INET, SOCK_DGRAM)
udp_recv_socket.bind(address)
while True:
    print("等待数据")
    data, send_address = udp_recv_socket.recvfrom(buf_size)
    print(data.decode("utf-8"))
    str1 = input('服务器端输入数据:')
    udp_recv_socket.sendto(str1.encode('utf-8'),send_address)



from socket import *
import _ip

port = 8890
address = (_ip.ip, port)
port1 = 8899
udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(address)
while True:
    print('等待客户发送数据...')
    data, send_address = udp_socket.recvfrom(1024)
    print('来自:%s' % str(send_address))
    print('消息:%s' % data.decode('utf-8'))
    msg = input('请输入:')
    udp_socket.sendto(msg.encode('utf-8'), (_ip.ip, port1))
udp_socket.close()

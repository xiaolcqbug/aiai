from socket import *
import _ip

port = 8890
address = (_ip.ip, port)
port1 = 8899
udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind((_ip.ip, port1))
while True:
    msg = input('请输入:')
    if not msg:
        print('结束发送放程序...')
        break
    udp_socket.sendto(msg.encode('utf-8'), address)
    data = udp_socket.recvfrom(1024)

    print('服务器发送的:%s' % data[0].decode('utf-8'))
udp_socket.close()

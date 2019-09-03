from socket import *



cip = 'localhost'
port = 8888
address = (cip,port)
size = 1024


udp_socket = socket(AF_INET,SOCK_DGRAM)
udp_socket.bind(address)


while True:
    data,send_addres = udp_socket.recvfrom(size) #recvfrom  接收数据
    res = data.decode('utf8')
    print('来自:%s发送的消息: %s'%(str(send_addres),res))
    if res == 'over':
        break


udp_socket.close()


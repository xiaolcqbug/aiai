from socket import *
ip='127.0.0.1'
port=8090
address=(ip,port)
buf_size=1024


udp_socket=socket(AF_INET,SOCK_DGRAM)
udp_socket.bind(address)
while True:
    data,link= udp_socket.recvfrom(buf_size)
    print('有人说',data.decode('utf8'))
    msg=input('..')
    udp_socket.sendto(msg.encode('utf8'),link)
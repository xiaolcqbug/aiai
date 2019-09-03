from socket import *

ip='localhost'
port=7777
address=ip,port
buf_size=1024
udp_socket=socket(AF_INET,SOCK_DGRAM)
udp_socket.bind(address)

while 1:
    print('等待别人向我发数据')
    con,con_addr=udp_socket.recvfrom(buf_size)
    print('来自:%s 发来的消息:%s'%(str(con_addr),con.decode('utf8')))
    continue

udp_socket.close()
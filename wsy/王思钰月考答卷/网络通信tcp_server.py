from socket import *

ip = '192.168.1.24'
prot = 4407
add = (ip,prot)
buf_size = 1024

tcp_socket = socket(AF_INET,SOCK_STREAM)
tcp_socket.bind(add)
tcp_socket.listen(5)


print('等待大雄连接')
c_socket,c_add = tcp_socket.accept()
print('这是来自大雄%s的连接'%str(c_add))


# 收发消息
while 1:
    data = c_socket.recv(buf_size)
    data = data.decode('utf_8')
    print('哆啦A梦传来信息:%s'%data)



c_socket.close()
tcp_socket.close()
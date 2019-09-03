
from socket import *

ip = '127.0.0.1'
prot = 56442
add = (ip,prot)
buf_size = 1024

tcp_socket = socket(AF_INET,SOCK_STREAM)

tcp_socket.bind(add)

tcp_socket.listen(5)

print('等待连接')
c_socket,c_add = tcp_socket.accept()
print('这是来自%s的连接'%str(c_add))

while 1:
    data = c_socket.recv(buf_size)
    data = data.decode('utf_8')
    print('客户端传来信息:%s'%data)
    if data=='over':
        print('服务器退出中..')
        break
    msg = input('请服务器输入：')
    c_socket.send(msg.encode('utf_8'))

c_socket.close()
tcp_socket.close()
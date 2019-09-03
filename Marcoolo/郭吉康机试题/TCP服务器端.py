from socket import *

ip = '127.0.0.1'
port = 12345
add = (ip, port)
buf_size = 1024
tcp_socket = socket(AF_INET, SOCK_STREAM)

# 绑定
tcp_socket.bind(add)
# 监听
tcp_socket.listen(5)
# 等待客户端连接的到来.
c_socket, c_add = tcp_socket.accept()

while 1:
    data = c_socket.recv(buf_size)
    data = data.decode('utf-8')
    print('客户端传来的信息:%s' % data)
    if data == 'over':
        print('服务器退出中..')
        break
    msg = input('服务器输入:')
    c_socket.send(msg.encode('utf-8'))


c_socket.close()
tcp_socket.close()
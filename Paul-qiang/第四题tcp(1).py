from socket import *

ip = '192.168.1.18'
port = 8089

add = (ip, port)
bufsize = 1024

# 创建tcp 套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)

# 绑定  监听   准备接入
tcp_socket.bind(add)
tcp_socket.listen(50)

# 接收数据
while 1:
    print('befor accept--')
    con, c_add = tcp_socket.accept()
    print('afer accept')
    data_bytes = con.recv(bufsize)
    data = data_bytes.decode('utf8')
    print('data:', data)
    print('客户端是来自:', c_add)

    con.send('你好:{}'.format(c_add[0]).encode('utf8'))
    con.send('你好:{}'.format(data).encode('utf8'))

    con.close()
tcp_socket.close()

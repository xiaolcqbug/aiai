from socket import *

ip = '127.0.0.1'
port = 8089

add = (ip, port)
buf_size = 10

# 创建tcp 套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)

# 绑定  监听   准备接入
tcp_socket.bind(add)
tcp_socket.listen(5)
print('befor accept--')
con, c_add = tcp_socket.accept()
print('afer accept')

# 接收数据
data_bytes1 = con.recv(bufsize)
data_bytes2 = con.recv(bufsize)
print('data_bytes1:',data_bytes1)
print('data_bytes2:',data_bytes2)
print('客户端是来自:', c_add)

con.close()
tcp_socket.close()

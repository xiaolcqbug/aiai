from socket import *
host = '127.0.0.1'
port = 3302
add = (host,port)
tcp_socket = socket(AF_INET,SOCK_STREAM)
tcp_socket.bind(add)
tcp_socket.listen(3)
print('等待客户端连接')
tcp_clisock , cli_add = tcp_socket.accept()
print('接收来自%s的连接',(cli_add,))
while True:
    data = tcp_clisock.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))
    mas = input('服务器输入:')
    tcp_clisock.send(mas.encode('utf-8'))
tcp_socket.close()
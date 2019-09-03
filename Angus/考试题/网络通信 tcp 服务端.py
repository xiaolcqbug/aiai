from socket import *
import _ip

tcp_socket = socket(AF_INET, SOCK_STREAM)
port = 7789
address = (_ip.ip, port)
tcp_socket.bind(address)
tcp_socket.listen(5)
print('等待连接....')

while True:
    tcp_client, adrs = tcp_socket.accept()
    print('来自%s的连接...' % str(adrs))
    res = tcp_client.recv(1024)
    print(res.decode('utf-8'))
    msg = input('请输入:')
    tcp_client.send(msg.encode('utf-8'))
tcp_client.close()
tcp_socket.close()

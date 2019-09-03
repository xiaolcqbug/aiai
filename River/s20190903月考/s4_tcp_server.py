from socket import *

ip='127.0.0.1'
port=54321
address=(ip,port)
buf_size=1024

tcp_server_socket=socket(AF_INET,SOCK_STREAM)
tcp_server_socket.bind(address)

tcp_server_socket.listen(5)

print('---等待客户端的链接---')

client_socket,client_address=tcp_server_socket.accept()
print('来自%s的链接....'% str(client_address))
while True:
    data=client_socket.recv(buf_size)
    data=data.decode('utf-8')
    print('客户端说：', data)
    msg = input('请输入:')
    client_socket.send(msg.encode('utf-8'))

client_socket.close()
tcp_server_socket.close()
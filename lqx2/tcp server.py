from socket import *

ip='127.0.0.1'
port=6767
address=(ip,port)
byte_size=100
tcp_socket=socket(AF_INET,SOCK_STREAM)
tcp_socket.bind(address)
tcp_socket.listen(10)
print('等待客户端发消息')
while 1:
    con,send_address=tcp_socket.accept()
    res=con.recv(byte_size).decode('utf8')
    print(res)
    con.close()
    continue

tcp_socket.close()

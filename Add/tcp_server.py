from socket import *
import time
ip='localhost'
port=8888
address=(ip,port)
buf_size=1024
tcp_socket=socket(AF_INET,SOCK_STREAM)
tcp_socket.bind(address)
tcp_socket.listen(10)
print('等待客户端连接..')


while 1:
    con, con_addr = tcp_socket.accept()
    data1=con.recv(buf_size).decode('utf8')
    print('来之{}发来的消息'.format(con_addr))
    print(data1)

    con.close()
    continue
tcp_socket.close()




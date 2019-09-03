from socket import *
from threading import Thread
ip='127.0.0.1'
port=9630
address=(ip,port)
buf_size=1024
def server1():
    print('等待连接')
    tcp_socket_server = socket(AF_INET, SOCK_STREAM)
    tcp_socket_server.bind(address)
    tcp_socket_server.listen(10)
    con, cadd = tcp_socket_server.accept()
    while 1:

        data1=con.recv(buf_size)
        data1=data1.decode('utf-8')
        print('收到来自{}的消息{}'.format(cadd,data1))
        if data1=='exit':
            print('客户端退出聊天')
            break

        msg=input('请输入服务器返回客户端的消息')
        msg=msg.encode('utf-8')
        con.send(msg)


            # con.close()
            # tcp_socket_server.close()
if __name__ == '__main__':
    Thread(target=server1).start()
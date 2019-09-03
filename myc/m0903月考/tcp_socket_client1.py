from socket import *
from threading import Thread
ip='127.0.0.1'
port=9630
address=(ip,port)
buf_size=1024
tcp_socket_client=socket(AF_INET,SOCK_STREAM)

tcp_socket_client.connect(address)
def client1():
    while True:
        msg = input('请客户端输入:')
        msg=msg.encode('utf-8')
        tcp_socket_client.send(msg)
        res = tcp_socket_client.recv(buf_size)
        res = res.decode('utf-8')
        print('接收到服务器的消息%s'%(res))
        if res=='exit':
            print('服务器退出聊天')
            break

if __name__ == '__main__':
    Thread(target=client1).start()



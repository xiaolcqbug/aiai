from socket import *
from threading import Thread
ip='localhost'
port=9632
address=(ip,port)
def client_send():
    udp_socket_client=socket(AF_INET,SOCK_DGRAM)
    while True:
        msg = input("请输入消息：")
        if  msg=='exit':
            print("结束发送..")
            break
        msg=msg.encode("utf-8")
        udp_socket_client.sendto(msg, address)
        data, send_address = udp_socket_client.recvfrom(1024)
        data=data.decode('utf-8')
        print('接收到来自服务器的消息{}'.format(data))

if __name__ == '__main__':
    Thread(target=client_send).start()

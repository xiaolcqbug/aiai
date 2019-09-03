from socket import *
from threading import  Thread

ip = "localhost"
port = 9632
address = (ip, port)
buf_size = 1024

udp_recv_socket = socket(AF_INET, SOCK_DGRAM)
udp_recv_socket.bind(address)

def server_recv():
    while True:
        print("等待接受消息..")
        data, send_address = udp_recv_socket.recvfrom(buf_size)
        data=data.decode('utf-8')
        print("来自：%s 发送来的消息：%s" % ((send_address), data))
        if data=='exit':
            print('客户端退出聊天')
            break
        res= input('服务器输入消息:')
        res=res.encode('utf-8')
        udp_recv_socket.sendto(res,send_address)

if __name__ == '__main__':
    Thread(target=server_recv).start()



from socket import *

ip = "192.168.1.24"
port = 4406
address = (ip, port)

udp_send_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input("熊二发送消息：")
    if not msg:
        print("聊天结束..")
        break
    # 发送
    udp_send_socket.sendto(msg.encode("utf-8"), address)
    data, send_address=udp_send_socket.recvfrom(1024)
    print('熊大发来消息:{}'.format(data.decode('utf-8')))

udp_send_socket.close()

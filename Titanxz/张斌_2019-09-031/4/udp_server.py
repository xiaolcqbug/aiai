#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2019/9/3 14:45:47
# @License :   (C) Copyright 2019, {python_1904}


# 网络通信   发     udp

from setting import *

udp_server_socket = socket(AF_INET, SOCK_DGRAM)
udp_server_socket.bind(address)

while 1:
    print("等待客户端发送的数据...")
    data, send_address = udp_server_socket.recvfrom(buf_size)  # udp接收数据，返回值是一个元组(data,发送方)
    print("来自客户端：%s 发送来的消息：\n%s" % (str(send_address), data.decode("utf-8")))
    str1 = input('服务器端说: ')
    udp_server_socket.sendto(str1.encode('utf-8'),send_address)

udp_server_socket.close()
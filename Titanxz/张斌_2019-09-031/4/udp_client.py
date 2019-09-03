#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2019/9/3 14:46:09
# @License :   (C) Copyright 2019, {python_1904}


# 网络通信   收   udp

from setting import *

udp_client_socket = socket(AF_INET, SOCK_DGRAM)

while 1:
    msg = input('客户端说: ')
    if not msg:
        print('客户端已退出...')
        break
    udp_client_socket.sendto(msg.encode('utf8'), address)
    data, server_address = udp_client_socket.recvfrom(buf_size)
    print('服务器说: {}'.format(data.decode('utf-8')))
udp_client_socket.close()

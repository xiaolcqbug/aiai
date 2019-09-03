#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2019/9/3 14:45:35
# @License :   (C) Copyright 2019, {python_1904}


# 网络通信   收   tcp

from setting import *

tcp_client_socket = socket(AF_INET, SOCK_STREAM)
tcp_client_socket.connect(address)

while 1:
    msg = input('客户端说: ')
    if not msg:
        print('客户端已退出...')
        break
    tcp_client_socket.send(msg.encode('utf8'))
    data = tcp_client_socket.recv(buf_size)
    data = data.decode('utf8')
    print('服务端说: ', data)

tcp_client_socket.close()
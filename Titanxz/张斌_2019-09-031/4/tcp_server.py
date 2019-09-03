#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  :   {Titanxz}
# @Time    :   2019/9/3 14:43:37
# @License :   (C) Copyright 2019, {python_1904}


# 网络通信   发    tcp

from setting import *

tcp_server_socket = socket(AF_INET, SOCK_STREAM)
tcp_server_socket.bind(address)
tcp_server_socket.listen(5)
print('服务器等待连接...')
client_socket, client_address = tcp_server_socket.accept()
print('{} 已连接'.format(client_address))
while 1:
    data = client_socket.recv(buf_size)
    if not data:
        print('客户端已退出...')
        break
    data = data.decode('utf8')
    print('客户端说: ', data)
    msg = input('服务器说: ')
    client_socket.send(msg.encode('utf8'))
client_socket.close()
tcp_server_socket.close()
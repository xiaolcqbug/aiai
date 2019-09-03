import socket


# 获取本机计算机名
hostname = socket.gethostname()
    # 获取本机ip
ip = socket.gethostbyname(hostname)

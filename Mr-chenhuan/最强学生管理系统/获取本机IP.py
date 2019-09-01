import socket
import pymysql

# 获取本机计算机名称
hostname = socket.gethostname()
# 获取本机ip
ip = socket.gethostbyname(hostname)
print(ip)
#169.254.131.53

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip
# print(get_host_ip())            # 192.168.1.28
# print(type(get_host_ip()))      # <class 'str'>


# pymysql.set_max_connections(31)
# 设置允许同时连接到数据库的链接的最大数量。默认是25。
# 这是pymssql对于DB-API 2.0的扩展)
# a = 'werwr{}'




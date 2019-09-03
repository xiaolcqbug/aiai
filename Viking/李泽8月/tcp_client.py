import socket

ip = '192.168.1.13'
port = 8080
adder = ('192.168.1.13', 8080)

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(adder)
text = input('输入:')
tcp_socket.send(text.encode('utf8'))
mess = tcp_socket.recv(1024)
print(mess.decode('utf8'))
tcp_socket.close()

import socket

ip = '192.168.1.13'
port = 8080
adder = ('192.168.1.13', 8080)

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(adder)
tcp_socket.listen(5)
new_socket, adder = tcp_socket.accept()
mess = new_socket.recv(1024)
print(mess.decode('utf8'))
new_socket.send(mess)
new_socket.close()
tcp_socket.close()

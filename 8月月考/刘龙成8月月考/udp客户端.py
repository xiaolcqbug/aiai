from socket import *

udp_clinet = socket(AF_INET, SOCK_DGRAM)
udp_clinet.sendto(b'123', ('localhost', 9999))
udp_clinet.close()

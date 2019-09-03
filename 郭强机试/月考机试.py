# from multiprocessing import Process
# 第一种
# def task1():
#     print('python!')
#
# def task2():
#     print('--python')
#
# if __name__ == '__main__':
#     p1=Process(target=task1)
#     p2=Process(target=task2)
#     p1.start()
#     p2.start()
# 第二种:
# class Myprocess(Process):
#
#     def __init__(self,x,y):
#         # Process.__init__(self)
#         super(Myprocess, self).__init__()
#         self.x = x
#         self.y = y
#
#
#     def run(self):
#         for i in range(self.x,self.y):
#             print('i:',i)
#
#     def run1(self):
#         print('wwwwwwww')
#
#
# if __name__ == '__main__':
#     p1 = Myprocess(5,10)
#     p1.start()
#     print(p1)
#     print(p1.name)
#     print






# from threading import  Thread
#
# def task1():
#     print('python')
#
# def task2():
#     print('---python')
#
# if __name__ == '__main__':
#     p1=Thread(target=task1)
#     p2=Thread(target=task2)
#     p1.start()
#     p2.start()





 # class MYThread(Thread):
#
#     def __init__(self,x,y):
#         # Process.__init__(self)
#         super(MyThread, self).__init__()
#         self.x = x
#         self.y = y
#
#
#     def run(self):
#         for i in range(self.x,self.y):
#             print('i:',i)
#
#     def run1(self):
#         print('wwwwwwww')
#
#
# if __name__ == '__main__':
#     p1 = MyThread(5,10)
#     p1.start()
#     print(p1)
#     print(p1.name)
#     print
#
# from socket import *
# ip='192.168.1.32'
# port=8089
# add=(ip,port)
# tcp_socket=socket(AF_INET,SOCK_STREAM)
# tcp_socket.connect(add)
# res=tcp_socket.send(b'abcdefg')
# print(res)
# tcp_socket.close()

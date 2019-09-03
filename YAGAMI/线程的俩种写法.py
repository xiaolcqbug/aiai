from threading import Thread
from multiprocessing import Process
import time

def task1(play):
    print('玩了{}'.format(play))
if __name__ == '__main__':
    start = time.time()
    t = Thread(target=task1,args=('lol',))
    t.start()
    t1 = Process(target=task1,args=('dnf',))
    t1.start()


#
# class MyTread(Thread):
#     def __init__(self,n):
#         super(MyTread, self).__init__()
#         self.n = n
#
#     def run(self):
#         for i in range(self.n):
#             print('hello python')
#
# if __name__ == '__main__':
#     t = MyTread(6)
#     t.start()

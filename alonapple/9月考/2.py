# 线程两种写法
import threading

def a():
    print('哈哈')
def b():
    print('呵呵')
t1=threading.Thread(target=a)
t2=threading.Thread(target=b)
t1.start()
t2.start()

from threading import Thread
class mythead(Thread):
    def __init__(self, name):
        super(mythead, self).__init__()
        self.name = name
    def run(self):
        print('哈喽', self.name)

if __name__ == '__main__':
    t1 = mythead('1')
    t2 = mythead('2')
    t1.start()
    t2.start()

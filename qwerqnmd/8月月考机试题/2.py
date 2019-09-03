# 线程两种写法
from threading import Thread

# 函数
def task1(food):
    print('我去....{}'.format(food))

if __name__ == '__main__':
    t = Thread(target=task1, args=('哈哈哈',))
    t.start()

#类
class MyThread(Thread):
    def __init__(self,food):
        Thread.__init__(self)
        self.food = food
    def run(self):
        print('我去.....{}'.format(self.food))

if __name__ == '__main__':

    t = MyThread('哈哈哈')
    t.start()

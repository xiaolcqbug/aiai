# 进程两种写法
from multiprocessing import Process


# 类方法
#
class MyProcess(Process):
    def __init__(self,food):
        Process.__init__(self)
        self.food = food
    def run(self):
        print('我去....{}'.format(self.food))

if __name__ == '__main__':

    q = MyProcess('哈哈哈')
    q.start()

# 函数方法


def shushu(x,y):
    for i in range(x,y):
        print(i)

if __name__ == '__main__':
    p1 = Process(target=shushu,args=(1,5))
    p1.start()

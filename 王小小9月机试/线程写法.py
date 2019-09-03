#第一种
from threading import Thread

# def task1(food):
#     print('吃饭...{}'.format(food))
# if __name__ == '__main__':
#     t = Thread(target=task1,args=('火鸡面',))
#     t.start()

# 第二种
class Count1(Thread):
    def __init__(self,two1):
        super(Count1, self).__init__()
        self.two1 = two1
    def run(self):
        print('runing task',self.two1)

p1 = Count1(1)
p1.start()

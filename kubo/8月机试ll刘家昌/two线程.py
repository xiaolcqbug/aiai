# 线程两种写法
from threading import Thread
import time


# def task1():
#     print('吃饭（第一种线程写法)')
#
#
# def task2():
#     print('喝水(第一种线程写法)')
#
#
# if __name__ == '__main__':
#     p1 = Thread(target=task1)
#     p2 = Thread(target=task2)
#     p1.start()
#     p2.start()

# 第二种线程写法

class mytheard(Thread):
    def run(self):
        print('第二种线程写法')


if __name__ == '__main__':
    p = mytheard()
    p.start()

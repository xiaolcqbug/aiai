# 进程两种写法
from multiprocessing import Process
import time


# def task1():
#     print('第一种进程写法')
#
#
# def task2():
#     print('第一种进程写法2')
#
#
# if __name__ == '__main__':
#     t1 = Process(target=task1)
#     t2 = Process(target=task2)
#     t1.start()
#     time.sleep(2)
#     t2.start()


# 第二种进程写法
class task(Process):
    def run(self):
        print('第二种写法')


if __name__ == '__main__':
    p1 = task()
    p1.start()

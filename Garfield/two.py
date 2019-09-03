# 线程的两种写法
from threading import Thread


# 第一种
def task1():
    print('线程开启')


if __name__ == '__main__':
    p1 = Thread(target=task1)
    p1.start()


# 第二种
class MyThread(Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        print('线程开启')


if __name__ == '__main__':
    p1 = MyThread()
    p1.start()

# 进程的两种写法
from multiprocessing import Process


# 第一种
def task1():
    print('进程开启')


if __name__ == '__main__':
    p1 = Process(target=task1)
    p1.start()


# 第二种
class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        print('进程开启')


if __name__ == '__main__':
    p1 = MyProcess()
    p1.start()

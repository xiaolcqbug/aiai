# 进程两种写法

# 第一种写法
from multiprocessing import Process


def task1():
    for i in range(0, 100):
        print(i)


if __name__ == '__main__':
    p1 = Process(target=task1)
    p1.start()

# 第二种写法
from multiprocessing import Process


class Task2(Process):
    def run(self):
        for i in range(0, 100):
            print('i:', i)


if __name__ == '__main__':
    p2 = Task2()
    p2.start()

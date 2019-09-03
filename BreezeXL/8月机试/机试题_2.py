#  线程两种写法

# 第一种写法
from threading import Thread


def task1(food):
    print('吃{}......'.format(food))


if __name__ == '__main__':
    t1 = Thread(target=task1, args=('薯片',))
    t1.start()

# 第二种写法
from threading import Thread


class Task2(Thread):
    def __init__(self, food):
        Thread.__init__(self)
        self.food = food

    def run(self):
        print('吃{}......'.format(self.food))


if __name__ == '__main__':
    t2 = Task2('薯条')
    t2.start()

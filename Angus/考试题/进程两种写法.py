# 进程的两种写法
from multiprocessing import Process


def run(sum):
    for i in range(sum):
        print(i)


if __name__ == '__main__':
    p1 = Process(target=run, args=(10,))
    p1.start()


class My_process(Process):
    def __init__(self, sum):
        # Process.__init__(self)
        super(My_process, self).__init__()
        self.sum = sum

    def run(self):
        for i in range(self.sum):
            print(i)


if __name__ == '__main__':
    m = My_process(10)
    m.start()


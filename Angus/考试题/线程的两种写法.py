# 线程的两种写法
from threading import Thread


def run(sum):
    for i in range(sum):
        print(i)


if __name__ == '__main__':
    t = Thread(target=run, args=(10,))
    # t.start()


class My_thread(Thread):
    def __init__(self, sum):
        # Thread.__init__(self)
        super(My_thread, self).__init__()
        self.sum = sum

    def run(self):
        for i in range(self.sum):
            print(i)
if __name__ == '__main__':
    m=My_thread(10)
    m.start()

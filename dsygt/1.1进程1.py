from multiprocessing import Process
# 进程，通过类来写


def shushu(x, y):
    for i in range(x, y):
        print(i)


class MyProcess(Process):
    def __init__(self, x, y):
        # Process.__init__(self)  # 父类初始化
        super(MyProcess, self).__init__()
        self.x = x
        self.y = y

    def run(self):
        for i in range(self.x, self.y):
            print(i)


if __name__ == '__main__':
    # p1 = Process(target=shushu, args=(10, 15))  #args为元祖!!!
    # p1.start()

    p2 = MyProcess(10, 15)
    p2.start()

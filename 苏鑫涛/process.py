from multiprocessing import Process


def fun1():
    for i in range(5):
        print(i)


class Myprocess(Process):
    def run(self):
        for i in range(5, 10):
            print(i)


if __name__ == '__main__':
    p1 = Process(target=fun1)
    p1.start()
    m1 = Myprocess()
    m1.start()

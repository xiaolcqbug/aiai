from threading import Thread


def fun1():
    for i in range(5):
        print(i)


class Myprocess(Thread):
    def run(self):
        for i in range(5, 10):
            print(i)


if __name__ == '__main__':
    p1 = Thread(target=fun1)
    p1.start()
    m1 = Myprocess()
    m1.start()

from multiprocessing import Process


def fun1():
    print('第一种写法')


class Casual(Process):
    def run(self):
        print('第二种写法')


def main():
    p1 = Process(target=fun1, )
    p2 = Casual()
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()

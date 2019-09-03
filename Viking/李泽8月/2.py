from threading import Thread


def fun1():
    print('第一种写法')


class Casual(Thread):
    def run(self):
        print('第二种写法')


def main():
    t1 = Thread(target=fun1)
    t2 = Casual()
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()

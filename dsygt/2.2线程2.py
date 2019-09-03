from threading import Thread


# 线程通过函数来写
def sum(x, y):
    print(x + y)


if __name__ == '__main__':
    p1 = Thread(target=sum, args=(3, 5))
    p1.start()

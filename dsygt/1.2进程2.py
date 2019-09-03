from multiprocessing import Process
# 进程，通过函数来写

# 数数,从x-->y
def sing(x):
    print('我喜欢唱歌,最喜欢{}'.format(x))


def dance():
    print('dance.............')


if __name__ == '__main__':
    p1 = Process(target=sing, args=('中华大地',))
    p1.start()

    p2 = Process(target=dance)
    p2.start()

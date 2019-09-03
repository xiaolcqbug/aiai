from multiprocessing import Process
a = 0
def one_process():
    global a
    for i in range(10):
        a += 1
    print(a)
def two_process():
    global a
    for i in range(10):
        a += 2
    print(a)

if __name__ == '__main__':
    p1 = Process(target=one_process)
    p1.start()
    p2 = Process(target=two_process)
    p2.start()
    print(a)
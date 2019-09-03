from multiprocessing import Process

a = 0
def run2():
    global a
    for a in range(10):
        a += 1
    print('run2:',a)
def run3():
    global a
    for a in range(10):
        a += 2
    print('run3:',a)
if __name__ == '__main__':
    r2 = Process(target=run2)
    r3 = Process(target=run3)
    r2.start()
    r3.start()
    print(a)

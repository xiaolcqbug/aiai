from multiprocessing import Process

num = 0

def add_one():
    global num
    for n in range(10):
        num += 1
    print(num)


def add_two():
    global num
    for n in range(10):
       num +=  2
    print(num)


if __name__ == '__main__':
    p1 = Process(target=add_one)
    p2 = Process(target=add_two)
    p1.start()
    p2.start()









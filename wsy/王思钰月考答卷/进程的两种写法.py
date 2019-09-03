# (1)
from multiprocessing import Process

class Task(Process):
    def run(self):
        for i in range(0, 10):
            print(i)


if __name__ == '__main__':
    p1 = Task()
    p1.start()


# (2)
# from multiprocessing import Process
#
# def task2():
#     for i in range(0, 10):
#         print(i)
#
# if __name__ == '__main__':
#     p1 = Process(target=task2)
#     p1.start()


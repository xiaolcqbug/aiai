# 第一种
# from  multiprocessing import  Process
# from time import *
#
#
# def uncle():
#     for i in range(0, 500):
#         print(i)
#         # sleep(1)
#
#
# def uncle2():
#     for i in range(0, 500):
#         print('------>', i)
#         # sleep(1)
#
#
# if __name__ == '__main__':
#     p1 = Process(target=uncle, name='uncle1')
#     p1.start()
#
#     p2 = Process(target=uncle2)
#     p2.start()
#     sleep(5)
#     # print(p1)
#     print(p1.name)
#     print(p2.name)

# 第二种写法
from multiprocessing import Process



class Task2(Process):
    def run(self):
        for i in range(0, 100):
            print('i:', i)



if __name__ == '__main__':
    p1 = Task2()
    p1.start()
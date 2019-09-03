#第一种
from multiprocessing import Process
# def shushu():
#     for i in range(0,10):
#         print(i)
#
# if __name__ == '__main__':
#     p1 = Process(target=shushu,name='shu1')
#     p1.start()
#     p2 = Process(target=shushu)
#     p2.start()

# 第二种
class count1(Process):
    def run(self):
        for i in range(0, 10):
            print('i',i)
if __name__ == '__main__':
    p1 = count1()
    p1.start()
    print(p1)

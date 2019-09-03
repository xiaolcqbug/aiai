# 第一种
# from threading import Thread
# import time
#
# # 函数版
# def num():
#     # time.sleep(1)
#     for i in range(1,52):
#         time.sleep(1)
#         global a1
#         if i %2 != 0:
#             a1 = ('输出格式为:{}{}'.format(x, x+1))
#             # print(a1)  # <class 'str'>
#             continue
#
# def eng():
#     time.sleep(2)       #为了让a1出来
#     global a1
#     for d in range(65, 91):
#         b1 = chr(d)
#         print(a1 + b1)          # <class 'str'>
#         time.sleep(2)
#     print('over....')
#
# if __name__ == '__main__':
#     t1=Thread(target=num)
#     t1.start()
#     t2=Thread(target=eng)
#     t2.start()

# 第二种
from threading import Thread
from multiprocessing import Process
import time

def task1(food):
    print('吃饭....{}'.format(food))


class MyThread(Thread):
    def __init__(self,food):
        # super(MyThread, self).__init__()
        Thread.__init__(self)
        self.food=food

    def run(self):
        print('吃饭....{}'.format(self.food))


if __name__ == '__main__':
    start = time.time()
    t2 = MyThread('手抓饼')
    t2.start()



    end = time.time()
    print('用时:', end - start)  # 0.01898932456970215

from multiprocessing import Process
import time
# def task1(shushu):
#     print('11')
#     time.sleep(3)
#     print('22')
#
# if __name__ == '__main__':
#     p = Process(target=task1)
#     p.start()


class MyProcess(Process):
    def run(self):
        print('11')
        time.sleep(3)
        print('22')
if __name__ == '__main__':
    p = MyProcess()
    p.start()


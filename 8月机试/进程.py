# 第一种
# from multiprocessing import Process
# import time
#
#
# def task(name):
#     print('%s is running' % name)
#     time.sleep(3)
#     print('%s is done' % name)
#
#
# if __name__ == '__main__':
#
#     p = Process(target=task, args=('子进程1',))
#     p.start()
#
#     print('主进程')


# 第二种
# from multiprocessing import Process
# import time
#
#
# class Myprocess(Process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print('%s is running' % self.name)
#         time.sleep(3)
#         print('%s is done' % self.name)
#
#
# if __name__ == '__main__':
#     p = Myprocess('子进程1')
#     p.start()
#
#     print('主进程')

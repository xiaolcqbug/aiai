#第一种
# from threading import Thread
# import time
#
#
# def s(name):
#     time.sleep(2)
#     print('%s say hello' % name)
#
#
# if __name__ == '__main__':
#     t = Thread(target=s, args=('li',))
#     t.start()
#     print('主线程')

#第二种
# from threading import Thread
# import time
#
#
# class s(Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         time.sleep(2)
#         print('%s say hello' % self.name)
#
#
# if __name__ == '__main__':
#     t = s('li')
#     t.start()
#     print('主线程')
#


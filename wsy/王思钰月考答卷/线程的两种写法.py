# (1)
from threading import Thread

def task():
    for i in range(0, 10):
        print(i)

p1 = Thread(target=task)
p1.start()

# (2)
# from threading import Thread
#
# class Student1(Thread):
#     def __init__(self,name):
#         super(Student1, self).__init__()
#         self.name = name
#     def run(self):
#         print('学习中...{}'.format(self.name))
#
# if __name__ == '__main__':
#     p1 = Student1('小明')
#     p1.start()
#
#

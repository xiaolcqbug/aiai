# 进程两种写法

from multiprocessing import Process
class Myprocess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print('我是子进程{}'.format(self.name))
if __name__ == '__main__':
    p = Myprocess('哈哈')
    p1 = Myprocess('哈哈2')
    p.start()
    p1.start()
    print("我是主进程")

from multiprocessing import Process
def eat():
    print('子进程')
if __name__ == '__main__':
    print('主进程')
    p1=Process(target=eat)
    p1.start()

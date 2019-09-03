from threading import Thread


# 函数
def target1(a):
    for i in range(a):
        print('qwer')

# if __name__ == '__main__':
#     t1 = Thread(target=target1,args=(3,))
#     t1.start()
    # qwer
    # qwer
    # qwer

# 类
class People():

    def __init__(self,int):
        super(People, self).__init__()
        self.int = int

    def run(self):
        print('张三跑了{}圈'.format(self.int))

if __name__ == '__main__':
    p1 = People(1)
    p1.run()



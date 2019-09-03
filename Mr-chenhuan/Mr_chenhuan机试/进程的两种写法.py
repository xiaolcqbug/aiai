from multiprocessing import Process

# 函数

def target1(a):
    for i in range(a):
        print('wwww')

if __name__ == '__main__':
    p1 = Process(target=target1,args=(3,))
    p1.start()
    # wwww
    # wwww
    # wwww


# 类
class People():

    def __init__(self,name):
        super(People, self).__init__()
        self.name = name

    def run(self):
        print('{}跑了10圈.'.format(self.name))

# if __name__ == '__main__':
#     p1 = People('张三')
#     p1.run()

#      张三跑了10圈.


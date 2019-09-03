from multiprocessing import Process  #导包

#第一种
def dosomething(x,y):
    for i in range(x,y):
        print('--------->',i)


if __name__ == '__main__':
    p1 = Process(target=dosomething,args=(10,15,))
    p1.start()
    p1.join()



#第二种

class Number(Process):  #继承process
    def __init__(self,x,y):
        # super(number, self).__init__()
        Process.__init__(self)
        self.x = x
        self.y = y

    def run(self):
        for i in range(self.x,self.y):
            print('*************>>',i)

if __name__ == '__main__':
    p1 = Number(10,15,)
    p1.start()
    p2 = Number(10,15,)



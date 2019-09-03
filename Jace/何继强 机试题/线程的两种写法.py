from threading import Thread  #导包

#第一种
def dosomething(x,y):
    for i in range(x,y):
        print('--------->',i)


if __name__ == '__main__':
    p1 = Thread(target=dosomething,args=(10,15,))
    p1.start()
    p1.join()



#第二种

class Number(Thread):  #继承process
    def __init__(self,x,y):
        # super(number, self).__init__()
        Thread.__init__(self)
        self.x = x
        self.y = y

    def run(self):
        for i in range(self.x,self.y):
            print('*************>>',i)

if __name__ == '__main__':
    p1 = Number(10,15,)
    p1.start()
    p2 = Number(10,15,)



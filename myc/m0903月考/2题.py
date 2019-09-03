# 线程两种写法

# from threading import Thread
#
# def eat(name,food):
#     print('{}在吃{}'.format(name,food))
#
# if __name__ == '__main__':
#     t1=Thread(target=eat,args=('沫沫','薯条'))
#     t1.start()
print('----------')
# from threading import Thread
#
# class Eat1(Thread):
#     def __init__(self,name,food):
#         Thread.__init__(self)
#         self.name=name
#         self.food=food
#
#     def run(self):
#         print('{}在吃{}'.format(self.name,self.food))
#
# if __name__ == '__main__':
#     t1=Eat1('小明','鸡腿')
#     t1.start()
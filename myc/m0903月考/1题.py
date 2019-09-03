# 1.进程两种写法
# from multiprocessing import Process
#
# def eat(who,what):
#     print('{}正在吃{}'.format(who,what))
#
# if __name__ == '__main__':
#     p1=Process(target=eat,args=('小明','肯德基'))
#     p1.start()
print('-----------------')

# from  multiprocessing import Process
#
# class Play1(Process):
#     def __init__(self,name,game):
#         super(Play1, self).__init__()
#         self.name=name
#         self.game=game
#
#     def run(self):
#         print('%s正在玩%s'%(self.name,self.game))
#
# if __name__ == '__main__':
#     p2=Play1('小明','LOL')
#     p2.start()
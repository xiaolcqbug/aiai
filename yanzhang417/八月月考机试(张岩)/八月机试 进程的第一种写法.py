from multiprocessing import Process
def task():
    print('哈哈')

if __name__ == '__main__':    #开进程要统一放到main方法的下面
    p=Process(target=task,args=('子进程',))
    p.start()


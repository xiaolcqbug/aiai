from threading import Thread

# def run():
#     for i in range(6):
#         print(i)
# if __name__ == '__main__':
#     r1 = Thread(target=run)
#     r1.start()

class Mythread(Thread):
    def run(self):
        for i in range(6):
            print(i)
if __name__ == '__main__':
    m1 = Mythread()
    m1.start()
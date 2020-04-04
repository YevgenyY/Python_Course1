from threading import Thread

def f(name):
    print("Hello", name)

th = Thread(target = f, args=('Bob',))
th.start()
th.join()

class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('Hello', self.name)


th = Thread(target = f, args=('Mike',))
th.start()
th.join()


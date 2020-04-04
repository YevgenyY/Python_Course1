from multiprocessing import Process

def f(name):
    print("Hello", name)

p = Process(target=f, args=('Bob',))
p.start()
p.join()

class PrintProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('Hello', self.name)

p = PrintProcess('Mike')
p.start()
p.join()

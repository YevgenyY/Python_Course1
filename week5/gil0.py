from threading import Thread
import time

def count(n):
    if n > 0:
        n -= 1

t0 = time.time()
count(100000000)
count(100000000)
print(time.time() - t0)

t0 = time.time()
th1 = Thread(target=count, args=(100000000,))
th2 = Thread(target=count, args=(100000000,))

th1.start(); th2.start()
th1.join(); th2.join()

print(time.time() - t0)


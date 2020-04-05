import time
import os

pid = os.fork()
if pid == 0:
    while True:
        print('child: ', os.getpid())
        time.sleep(51)

else:
    print('parent: ', os.getpid())
    os.wait()




class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()

with open_file('access.log', 'a') as f:
    f.write('Inside `open_file` context manager test log record\n')

class suppress_exception:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == self.exc_type:
            print('Got exception, do nothing')
            return True

with suppress_exception(ZeroDivisionError):
    increadible_bignum = 1 / 0
    print(increadible_bignum)

import contextlib
with contextlib.suppress(ValueError):
    raise ValueError

import time
class timer():
    def __init__(self):
        self.start = time.time()

    def current_time(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print('Elapsed: {}'.format(time.time() - self.start))


with timer() as t:
    time.sleep(1)
    t.current_time()

    #print('Current time: {}'.format( t.current_time() ))
    time.sleep(1)

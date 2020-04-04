import threading

a = threading.RLock()
b = threading.RLock()

def foo():
    try:
        a.acquire()
        b.acquire()
    finally:
        b.release()
        a.release()


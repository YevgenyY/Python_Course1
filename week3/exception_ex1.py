import traceback

try:
    with open("/file/not/found") as f:
        content = f.read()
except OSError as err:
    print(err.errno, err.strerror)
    trace = traceback.print_exc()
    print(trace)

try: 
    raw =input("enter a number: ")
    if not raw.isdigit():
        raise ValueError
except ValueError:
    print("Wrong number: {}".format(raw))

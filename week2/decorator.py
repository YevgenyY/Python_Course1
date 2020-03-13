import functools

def decorator(func):
    return func

@decorator
def decorated():
    print("Hello")

def logger(func):
    def wrapped(num_list):
        result = func(num_list)
        with open('log.txt', 'w') as f:
            f.write(str(result))

        return result
    return wrapped

@logger
def summator(num_list):
    return sum(num_list)

res = summator([1, 2, 3, 4, 5])
print(res)

def logger_any_args(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'w') as f:
            f.write(str(result))

        return result
    return wrapped


from functools import reduce

@logger_any_args
def multiplycator(num_list):
    def multiply(a, b):
        return a * b
    return reduce( multiply, num_list )

res = multiplycator([1,2,3,4,5])
print(res)

### Decorator with a parameter
def paralogger(filename):
    def decorator(func):
        def wrapped(*argc, **kwargs):
            result = func(*argc, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))

            return result
        return wrapped
    return decorator

@paralogger('newlog.txt')
def summator1(num_list):
    return sum(num_list)

res = summator1([1,2,3,4,5,6,7,8,9])
print(res)


def first_decorator(func):
    def wrapped():
        print('Inside the first decorator')
        return func()
    return wrapped

def second_decorator(func):
    def wrapped():
        print('Inside the second decorator')
        return func()
    return wrapped

@first_decorator
@second_decorator
def decorated_twice():
    print('Finally called')

decorated_twice()



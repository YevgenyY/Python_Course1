
def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2

for number in even_range(0, 10):
    print(number)

ranger = even_range(0, 4)

print( next(ranger) )
print( next(ranger) )

def list_generator(list_obj):
    for item in list_obj:
        yield item
        print('After yielding {}'.format(item))

generator = list_generator([1,2])
print( next(generator) )
print( next(generator) )

def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b

fibos = fibonacci(16)
print("Fibonacci numbers...")
for num in fibonacci(16):
    print( num )

def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value: break
        total += value

print("Accumulator numbers...")
generator = accumulator()

# init accumulator
next(generator)
# send number to accumulator
print( generator.send(1) )
print( generator.send(1) )


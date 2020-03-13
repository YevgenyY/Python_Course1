def squarify(a):
    return a ** 2

res = list( map(squarify, range(5)) )
print(res)

def is_positive(a):
    return a > 0

res = list( filter(is_positive, range(-2,3)) )
print(res)

res = list( map(lambda x: x**2, range(5)) )
print(res)

def list_to_string(a):
    return list( map(str, a) )

res = list_to_string( range(12) )
print(res)

from functools import reduce

def multiply(a, b):
    return a * b

res = reduce( multiply, [1, 2, 3, 4, 5] )
print(res)

from functools import partial

def greeter(person, greeting):
    return '{}, {}!'.format(greeting, person)

hier = partial(greeter, greeting='Hi')
helloer = partial(greeter, greeting='Hello')

print(hier('bro'))
print(helloer('sir'))

square_list = [ number ** 2 for number in range(10) ]
print(square_list)

square_map = { number: number**2 for number in range(5) }
print(square_map)

num_list = range(7)
squared_list = [ number ** 2 for number in num_list ]
list_obj =  list(zip(num_list, squared_list)) 
print(list_obj)

aaa = list( zip(filter(bool, range(3)), [x for x in range(3) if x] ) )
print(aaa)

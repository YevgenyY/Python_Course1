from datetime import datetime


def get_seconds():
    """return current seconds"""
    return datetime.now().second

def split_tags(tag_string):
    tag_list = []
    for tag in tag_string.split(','):
        tag_list.append(tag.strip())

    return tag_list

def add(x: int, y: int) -> int:
    return x + y

def printer(*args):
    print(type(args))
    for el in args:
        print(el)

print(get_seconds())

print( split_tags('python, coursera, mooc') )

printer(1, 2, 3, "four", 5)

namelist = ["John", "Bill", "Ammy"]
printer(*namelist)

def printdict(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print ('{}: {}'.format(key, value))

pl = {
    'user_id': 117,
    'feedback': {'subject': 'Registration fields',
                 'message': 'There is no fun for stupid men'
                 }
}
printdict(**pl)

printdict(a=10, b=12)


def foo(*args, **kwargs): 
    for el in args:
        print('args {}'.format(el))
    for key, value in kwargs.items():
        print ('{}: {}'.format(key, value))
    pass

foo(1, 2)
foo(a=1, b=2)



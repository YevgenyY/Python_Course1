class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email_data(self):
        return {
                'name':self.name,
                'email':self.email
                }

    def __str__(self):
        return '{} <{}>'.format(self.name, self.email)

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, obj):
        return self.email == obj.email

    def __getattr__(self, name):
        return 'Nothing found'

    def __getattribute__(self, name):
        print('Looking for attribute {}'.format(name))

        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        print('Gonna set smth {}'.format(name))

        return object.__setattr__(self, name, value)

    def __delattr__(self, name):
        value = getattr(self, name)
        print('Good bye {} you were {}'.format(name, value))

        return object.__delattr__(self, name)
    
class Logger:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            with open(self.filename, 'a') as f:
                f.write('Ohh I am gonna log it\n')

            return func(*args, **kwargs)
        return wrapped

logger = Logger('func_calls.log')

@logger
def useless_func():
    pass

useless_func()

jane = User('Jane Doe', 'jdoe@example.com')
joe = User('John Doe', 'jdoe@example.com')

print(jane.get_email_data())
print(jane)

class Singleton:

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

a = Singleton()
b = Singleton()

print(a is b)

print(jane == joe) # test __eq__ method

print(hash(jane))
print(hash(joe))

joe.delme = 123
del joe.delme



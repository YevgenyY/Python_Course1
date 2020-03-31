class Meta(type):
    def __init__(cls, name, bases, attrs):
        print('Initializing - {}'.format(name))

        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls

        super().__init__(name, bases, attrs)


class Base(metaclass=Meta): pass

class A(Base): pass
class B(Base): pass

print(Base.registry)
print(Base.__subclasses__())

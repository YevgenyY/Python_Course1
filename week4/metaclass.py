def dummy_factory():
    class Class:
        pass

    return Class

Dummy = dummy_factory()

# Classes are different
print(Dummy() is Dummy())

NewClass = type('NewClass', (), {})

print(NewClass)
print(NewClass())

class Meta(type):
    def __new__(cls, name, parents, attrs):
        print('Creating {}'.format(name))

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls, name, parents, attrs)

class Base(metaclass=Meta): pass

class A(Base): pass
class B(Base): pass

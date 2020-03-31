class Property:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, obj_type=None):
        if (obj is None):
            return self

        return self.getter(obj)

class Class:
    @property
    def original(self):
        return 'original'

    @Property
    def custom_salt(self):
        return 'custom salt'

    def custom_more(self):
        return 'custom more'

    custom_more = Property(custom_more)

obj = Class()

print(obj.original)
print(obj.custom_salt)
print(obj.custom_more)

class Descriptor:
    def __init__(self):
        self.value = None

    def __get__(self, obj, obj_type):
        print('get')
        return self.value

    @staticmethod
    def _prepare_value(value):
        return value * 10

    def __set__(self, obj, value):
        print('set')
        self.value = self._prepare_value(value)

    def __delete__(self, obj):
        print('delete')

class Class:
    attr = Descriptor()


instance = Class()
instance.attr
instance.attr = 10
print(instance.attr)

del instance.attr

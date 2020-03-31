class Value:
    def __init__(self):
        self.value = None
        
    @staticmethod
    def _prepare_value(value, comission):
        return value - value * comission

    def __set__(self, obj, value):
        #print('Set value')
        self.value = self._prepare_value(value, obj.commission)

    def __get__(self, obj, obj_type):
        return self.value



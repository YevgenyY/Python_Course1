
class PetExport:
    def export(self, dog):
        raise NotImplementedError


class Pet:

    def __init__(self, name=None):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return '{0}: woof, woof!'.format(self.name)


import json
class ExportJSON(PetExport):
    def export(self, dog):
        return json.dumps({
            "name":dog.name,
            "breed":dog.breed,
            })

class ExportXML(PetExport):
    def export(self, dog):
        return """<?xml version="1.0" encoding="utf-8"?>
<dog>
    <name>{0}</name>
    <breed>{1}</breed>
</dog>
    """.format(dog.name, dog.breed)

class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
       super().__init__(name, breed)
       self._exporter = exporter or ExportJSON()
       if not isinstance(self._exporter, PetExport):
           raise ValueError('bad exporter', exporter)

    def export(self):
       return self._exporter.export(self)

dog = ExDog('Sharik', 'wild', exporter=ExportXML())
doggy = ExDog('Tuzik', 'Mops')
print( dog.export() )
print( doggy.export() )


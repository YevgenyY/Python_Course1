
class Pet:

    def __init__(self, name=None):
        self.name = name

class Dog(Pet):
    def __init__(self, name=None, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return '{0}: woof, woof!'.format(self.name)


dog = Dog('Sharik')
print(dog.name)
print(dog.say())


# Multi inheritance
import json
class ExportJSON:
    def to_json(self):
        return json.dumps({
            'name': self.name,
            'breed': self.breed
            })

class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        # MRO call
        super().__init__(name, breed)
        # super(ExDog, self).__init__(name)

class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        # explicit call
        super(Dog, self).__init__(name)
        self.breed = 'Woolen dog breed {}'.format(breed)

dog = ExDog('Squirrel', breed='wild')
print(dog.to_json())
print(ExDog.__mro__)

wodog = WoolenDog('Zhuchka', breed='Taksa')
print(wodog.breed)


class Planet:
    count = 0

    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        self.name = name
        Planet.count += 1
        

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Planet {}'.format(self.name)

    #def __del__(self):
    #    print('Goodbye!')

earth = Planet("Earth")
print(earth.name)
print(earth)

solar_system = []
planet_names = ['Mercury', 'Venus', 'Earth', 'Mars',
                'Jupiter', 'Saturn', 'Uranus', 'Neptune'
                ]

for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)
print(Planet.count)
print(earth.count)

print(planet.__dict__)
print(Planet.__dict__)
print(earth.__class__)

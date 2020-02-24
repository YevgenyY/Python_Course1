empty_dict = {}
empty_dict = dict()

collections_map = {
            'mutable':['list', 'set', 'dict'],
            'immutable':['tuple', 'frozenset']
        }

print(collections_map)
print(collections_map['immutable'])
print(collections_map.get('notfound', 'not found'))


beatles_map = {
        'Paul' : 'Bass',
        'John' : 'Guitar',
        'George' : 'Guitar'
        }
print(beatles_map)

beatles_map['Ringo'] = 'Drums'
print(beatles_map)

del beatles_map['John']
print(beatles_map)

beatles_map.update({'John':'Guitar'})
print(beatles_map)

for key in beatles_map:
    print (key)

for key, value in collections_map.items():
    print( '{} - {}'.format(key, value)  )

collections = ['list', 'tuple', 'dict', 'set']

for collection in collections:
    print('Learning {}...'.format(collection))


for idx, collection in enumerate(collections):
    print('Learning #{} {}'.format(idx, collection))

collections.append('appended')
print(collections)

collections.extend(['elem1', 'elem2'])
print(collections)

collections += ['use_overloaded +']
print(collections)

print( ', '.join(collections) )

numbers = [1, 3, 5, 7, 11, 13, 17, 19]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

import random
nums = []
for _ in range(10):
    nums.append(random.randint(1, 20))

print(nums)
print(sorted(nums))
nums.sort(reverse=True)
print(nums)

# tuples

tuplex = ('one', 'two', [])
print(tuplex)
tuplex[2].append(['subone', 'subtwo'])
tuplex[2].append(['subthree'])
print(tuplex)


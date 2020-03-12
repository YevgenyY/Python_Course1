odd_set = set()
even_set = set()

for num in range(10):
    if num % 2:
        odd_set.add(num)
    else:
        even_set.add(num)

even_set.remove(2)

print(odd_set)
print(even_set)

union_set = odd_set | even_set
union1_set = odd_set.union(even_set)

print(union_set)
print(union1_set - odd_set)

frozen = frozenset(['Anna', 'Benna', 'Ganna']) # Can't change it after creation
print(frozen)

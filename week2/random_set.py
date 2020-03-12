import random

random_set = set()

while True:
    new_num = random.randint(1, 10)
    if new_num in random_set:
        break
    
    random_set.add(new_num)

print(len(random_set) +1)
        

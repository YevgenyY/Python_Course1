import random

class NoisyFloatList:
    def __init__(self, value):
        self.array = []
        self.array.append( value )

    def __getitem__(self, idx):
       noise = random.uniform(-1, 1)
       return self.array[idx] + noise

    def __setitem__(self, idx, value):
       noise = random.uniform(-1, 1)
       self.array[idx] = value + noise


a = NoisyFloatList(0)

for i in range(1, 12):
    a.array.append(i)

a[11]=0

for i in range(12):
    print(a[i])

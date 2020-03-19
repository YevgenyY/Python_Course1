%%timeit
my_dict = {"foo":1}

for i in range(1000):
    try:
        my_dict[i]
    except KeyError:
        pass

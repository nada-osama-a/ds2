import sorting
import random

sizes = [10000 , 25000, 50000, 100000]


def generate_arrays(size):
    return [random.randint(0, 100000) for _ in range(size)]

arrays = []
for size in sizes:
    arr = generate_arrays(size)
    arrays.append(arr)

 
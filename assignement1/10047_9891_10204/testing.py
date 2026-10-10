import sorting
import random
from time import time

sizes = [10000 , 25000, 50000, 100000]



def generate_arrays(size):
    return [random.randint(0, 100000) for _ in range(size)]



def measure_sort_time(sort_function, arr):
    start = time()
    sort_function(arr)
    end = time()
    sec = (end - start) * 1000
    return sec



for size in sizes:
    arr = generate_arrays(size)
    bubble_time = measure_sort_time(sorting.bubble_sort, arr.copy())
    selection_time = measure_sort_time(sorting.selection_sort, arr.copy())
    # insertion_time = measure_sort_time(sorting.insertion_sort, arr.copy())

    print(f"Array size: {size}")
    print(f"Bubble Sort time: {bubble_time:f} ms")
    print(f"Selection Sort time: {selection_time:f} ms")
    # print(f"Selection Sort time: {selection_time:f} ms")
    print()

 

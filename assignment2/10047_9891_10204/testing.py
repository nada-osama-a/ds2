import sort
import random
from time import time

sizes = [10000 , 25000, 50000, 100000]

def generate_arrays(size):
    return [random.randint(0, 100000) for _ in range(size)]

def measure_sort_time(sort_function, arr, threshold=None):
    start = time()
    if threshold is not None:
        sort_function(arr, threshold)
    else:
        sort_function(arr)
    end = time()
    sec = (end - start) * 1000
    return sec

for size in sizes:
    arr = generate_arrays(size)

    bubble_time = measure_sort_time(sort.bubble_sort, arr.copy())
    selection_time = measure_sort_time(sort.selection_sort, arr.copy())
    insertion_time = measure_sort_time(sort.insertion_sort, arr.copy())
    heap_time = measure_sort_time(sort.heap_sort, arr.copy())
    merge_time = measure_sort_time(sort.merge_sort, arr.copy())
    hybrid_time = measure_sort_time(sort.hybrid_merge_selection_sort, arr.copy(), threshold=10)

    print(f"Array size: {size}")
    print(f"Bubble Sort time: {bubble_time:f} ms")
    print(f"Selection Sort time: {selection_time:f} ms")
    print(f"Insertion Sort time: {insertion_time:f} ms")
    print(f"Heap Sort time: {heap_time:f} ms")
    print(f"Merge Sort time: {merge_time:f} ms")
    print(f"Hybrid Sort time: {hybrid_time:f} ms")
    print()
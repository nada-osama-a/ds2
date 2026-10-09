from time import time
import sorting

def measure_sort_time(sort_function, arr, sort_name):
    start = time()
    sort_function(arr)
    end = time()
    sec = (end - start) * 1000
    print(f"Sorted array using {sort_name}: {arr}")
    print(f"Running time is {sec} ms")

arr = [64, 34, 25, 12, 22, 11, 90, 0, -1, 100, 50, 75, 33, 44, 55]
measure_sort_time(sorting.bubble_sort, arr.copy(), "Bubble Sort")
measure_sort_time(sorting.selection_sort, arr.copy(), "Selection Sort") 
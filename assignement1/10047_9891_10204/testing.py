from time import perf_counter
import sorting

def measure_sort_time(sort_function, arr, sort_name):
    start_time = perf_counter()
    sort_function(arr)
    end_time = perf_counter()
    sec = (end_time - start_time) * 1000
    print(f"Sorted array using {sort_name}: {arr}")
    print(f"Running time is {sec:.3f} ms")

#arr = [64, 34, 25, 12, 22, 11, 90]
#measure_sort_time(sorting.bubble_sort, arr.copy(), "Bubble Sort")
#measure_sort_time(sorting.selection_sort, arr.copy(), "Selection Sort")
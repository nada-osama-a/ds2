import sort
import random
from time import time
import matplotlib.pyplot as plt

sizes = [1000, 25000, 50000, 100000]

def generate_arrays(size):
    return [random.randint(0, 100000) for _ in range(size)]

def measure_sort_time(sort_function, arr, threshold=None):
    start = time()
    if threshold is not None:
        sort_function(arr, threshold)
    elif sort_function == sort.quick_sort:
        sort_function(arr, 0, len(arr) - 1)
    else:
        sort_function(arr)
    end = time()
    sec = (end - start) * 1000
    return sec

results = {
    "Bubble Sort": [],
    "Selection Sort": [],
    "Insertion Sort": [],
    "Heap Sort": [],
    "Merge Sort": [],
    "Quick Sort": [],
    "Hybrid Sort": []
}

for size in sizes:
    arr = generate_arrays(size)

    b_time = measure_sort_time(sort.bubble_sort, arr.copy())
    s_time = measure_sort_time(sort.selection_sort, arr.copy())
    i_time = measure_sort_time(sort.insertion_sort, arr.copy())
    h_time = measure_sort_time(sort.heap_sort, arr.copy())
    m_time = measure_sort_time(sort.merge_sort, arr.copy())
    q_time = measure_sort_time(sort.quick_sort, arr.copy())
    hy_time = measure_sort_time(sort.hybrid_merge_selection_sort, arr.copy(), threshold=10)

    results["Bubble Sort"].append(b_time)
    results["Selection Sort"].append(s_time)
    results["Insertion Sort"].append(i_time)
    results["Heap Sort"].append(h_time)
    results["Merge Sort"].append(m_time)
    results["Quick Sort"].append(q_time)
    results["Hybrid Sort"].append(hy_time)

    print(f"Array size: {size}")
    print(f"Bubble Sort: {b_time:.2f} ms")
    print(f"Selection Sort: {s_time:.2f} ms")
    print(f"Insertion Sort: {i_time:.2f} ms")
    print(f"Heap Sort: {h_time:.2f} ms")
    print(f"Merge Sort: {m_time:.2f} ms")
    print(f"Quick Sort: {q_time:.2f} ms")
    print(f"Hybrid Sort: {hy_time:.2f} ms\n")

plt.figure(figsize=(10, 6))

for name, times in results.items():
    plt.plot(sizes, times, marker='o', label=name)

plt.xlabel('Input size (N)')
plt.ylabel('Execution time (ms)')
plt.title('Sorting Algorithms Execution Time Comparison')
plt.legend()
plt.grid(True)
# plt.savefig('sorting_comparison.png')
plt.show()
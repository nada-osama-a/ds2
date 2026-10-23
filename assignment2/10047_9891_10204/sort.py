def bubble_sort(arr):
    n = len(arr)

    a = arr.copy()
    for i in range(n):
        sorted = True
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                sorted = False
        if sorted:
            break
    return a

def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heap_sort(arr):
    a = arr.copy()
    n = len(a)
    build_max_heap(a)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        max_heapify(a, i, 0)

    return a                
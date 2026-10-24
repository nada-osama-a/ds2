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

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
 ###########################################################################
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
####################################################################

def merge_sort(arr):
    n=len(arr)
    if n < 2 :
        return
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:] 
    merge_sort(left)
    merge_sort(right)

    return merge(left, right, arr)

def merge(left, right, arr):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr
####################################################################

    
    
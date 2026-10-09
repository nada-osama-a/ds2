def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        sorted = True
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False
        if sorted:
            break
    return arr
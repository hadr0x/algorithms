def heap_sort(array):
    n = len(array)
    build_max_heap(array)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

def heapify(array, n, root):
    left = 2 * root + 1  
    right = 2 * root + 2
    largest = root

    if left < n and array[left] > array[root]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != root:
        array[largest], array[root] = array[root], array[largest]
        heapify(array, n, largest)

def build_max_heap(array):
    n = len(array)
    k = int(n // 2 - 1)

    for i in range(k, -1, -1):
        heapify(array, n, i)
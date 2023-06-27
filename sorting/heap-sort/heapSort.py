def heapSort(iterable):
    n = len(iterable)
    build_max_heap(iterable)

    for i in range(n - 1, 0, -1):
        iterable[i], iterable[0] = iterable[0], iterable[i]
        heapify(iterable, i, 0)
        
    return iterable

def heapify(iterable, n, root):
    left = 2 * root + 1  
    right = 2 * root + 2
    largest = root

    if left < n and iterable[left] > iterable[root]:
        largest = left

    if right < n and iterable[right] > iterable[largest]:
        largest = right

    if largest != root:
        iterable[largest], iterable[root] = iterable[root], iterable[largest]
        heapify(iterable, n, largest)

def build_max_heap(iterable):
    n = len(iterable)
    k = int(n // 2 - 1)

    for i in range(k, -1, -1):
        heapify(iterable, n, i)
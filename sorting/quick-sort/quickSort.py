def partition(iterable, low, high):

    # Rightmost element as pivot
    pivot = iterable[high]

    i = low - 1

    for k in range(low, high):
        if iterable[k] <= pivot:
            i = i + 1
            iterable[k], iterable[i] = iterable[i], iterable[k]

    iterable[i + 1], iterable[high] = iterable[high], iterable[i + 1]

    # Position where partition is done
    return i + 1


def quickSort(iterable, low, high):
    if low < high:
        
        pi = partition(iterable, low, high)

        # Recursive call on the left of pivot    
        quickSort(iterable, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(iterable, pi + 1, high)
        
    return iterable
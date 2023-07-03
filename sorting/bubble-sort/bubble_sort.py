def bubble_sort(iterable):
    for i in range(len(iterable) - 1):
    
        for k in range(0, len(iterable) - i - 1):
    
            if iterable[k] > iterable[k + 1]:
                iterable[k], iterable[k + 1] = iterable[k + 1], iterable[k]
    
    return iterable
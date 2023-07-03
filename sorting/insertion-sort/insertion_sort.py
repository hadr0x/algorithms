def insertion_sort(iterable):
    for i in range(len(iterable)):
        k = i
        
        while k > 0 and iterable[k - 1] > iterable[k]:
            iterable[k - 1],iterable[k] = iterable[k],iterable[k - 1]
            k = k - 1
    
    return iterable
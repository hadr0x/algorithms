def selection_sort(iterable):
    for i in range(len(iterable) - 1):

        for k in range(i, len(iterable)):

            if iterable[k] < iterable[i]:
                iterable[k], iterable[i] = iterable[i], iterable[k]

    return iterable
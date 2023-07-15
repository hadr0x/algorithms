def partition(array, low, high):

    # Rightmost element as pivot
    pivot = array[high]

    i = low - 1

    for k in range(low, high):
        if array[k] <= pivot:
            i = i + 1
            array[k], array[i] = array[i], array[k]

    array[i + 1], array[high] = array[high], array[i + 1]

    # Position where partition is done
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        
        pi = partition(array, low, high)

        # Recursive call on the left of pivot    
        quick_sort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)
        
    return array
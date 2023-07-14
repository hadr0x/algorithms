def bubble_sort(array):
    for i in range(len(array) - 1):
    
        for k in range(0, len(array) - i - 1):
    
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
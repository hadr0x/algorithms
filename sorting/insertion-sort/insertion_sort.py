def insertion_sort(array):
    for i in range(len(array)):
        k = i
        
        while k > 0 and array[k - 1] > array[k]:
            array[k - 1],array[k] = array[k],array[k - 1]
            k = k - 1
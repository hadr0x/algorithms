def selection_sort(array):
    for i in range(len(array) - 1):

        for k in range(i, len(array)):

            if array[k] < array[i]:
                array[k], array[i] = array[i], array[k]
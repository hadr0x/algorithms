def bubble_sort(A):
    for i in range(len(A) - 1):
    
        for k in range(0, len(A) - i - 1):
    
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]
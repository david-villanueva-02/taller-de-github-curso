def bubbleSort(A):
    n = len(A)
    flag    = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if A[j] > A[j + 1]:
                flag = True
                A[j], A[j + 1] = A[j + 1], A[j]
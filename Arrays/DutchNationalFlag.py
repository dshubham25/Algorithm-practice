def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    #First pass: group elements smaller than the pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    #Second pass: group elements larger than the pivot

    for i in reversed(range(len(A))):
        larger = 0
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
            
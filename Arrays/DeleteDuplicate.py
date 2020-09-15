def delete_duplicate(A):
    if not A:
        return 0
    index = 1
    for i in range(1, len(A)):
        if A[index - 1] != A[i]:
            A[index] = A[i]
            index += 1
    return index
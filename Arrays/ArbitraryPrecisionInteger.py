A = [1, 2, 9]
def plus_one(A):
    
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 0:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        #There is a carry-out
        #append 0 at the end of the array
        A[0] = 1
        A.appnd(0)
    return A

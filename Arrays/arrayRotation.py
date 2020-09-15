def leftRotate(arr, d, n):
    for _ in range(d):
        leftRotateOne(arr, n)


def leftRotateOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def printArray(arr, size):
    for i in range(size):
        print("% d"% arr[i], end=" ")

arr = [1, 2, 3, 4, 5, 6, 7, 8]
leftRotate(arr, 3, 7)
printArray(arr, 7)


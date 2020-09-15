def func_r(n):
    n = 5
    res = 0
    print("Start: " + str(n))
    if n == 0:
        res =  0
    else:
        res = func_r(n-1) + 1
    print("End: " + str(n))
    return res

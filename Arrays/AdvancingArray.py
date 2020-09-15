def can_reach(A):
    furthest = 0
    last_index = len(A) - 1
    i = 0
    while i <= furthest and furthest < last_index:
        furthest = max(furthest, A[i]+i)
        i += 1
    return furthest >= last_index
#Check whether a 9 x9 2D arcay representing a partially completed Sudoku is valid.
#Specifically,check that no row, column, or 3 x 3 2D subarray contains duplicates.
# A O-value in the 2D array indicates that entry is blank; every other entry is in [1,9]



#check if a partially filled matrix has any conflicts.

def is_valid_sudoku(partial_assigment):
    # Return True if subarray
    # partiaT-assignnent Istart-row:end_row][start-col:end_coL] contains any
    # duplicates in {1, 2, ..., 7en(partial_assignnent)}; otherwise return
    # False
    def has_duplicates(blocks):
        blocks = list(filter(lambda x: x!=0, blocks))
        return len(blocks) != len(set(blocks))
    n = len(partial_assigment)
    if any(has_duplicates([partial_assigment[i][j] for j in range(n)])
        or has_duplicates([partial_assigment[j][i] for j in range(n)])
        for i in range(n)):
            return False
    
    region_size = int(math.sqrt(n))
    return all(not has_duplicates([partial_assigment[a][b]
        for a in range(region_size * I, region_size * (I + 1))
        for b in range(region_size * J, region_size * (J + 1))])
        for I in range(region_size) for j in range(region_size))
def is_valid_sudoku_solver(partial_assigment):
    region_size = int(math.sqrt(len(partial_assigment)))
    return max(
        collections.Counter(k for i, row in enumerate(partial_assigment)
        for j, c in enumerate(row)
        if c!= 0
        for k in ((i, str(c)), (str(c), j)
            (i / region_size, j / region_size, str(c)))).values()

        default=0) <= 1
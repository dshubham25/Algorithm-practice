def matrix_rotation(square_matrix):
    matrix = len(square_matrix) - 1
    for i in range(len(square_matrix) // 2):
        for j in range(i, matrix - i):
            (square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j],
            square_matrix[j][~i]) = (square_matrix[~j][i],
                                    square_matrix[~i][~j],
                                    square_matrix[j][~i], square_matrix[i][j])

#T.C- O(n^2)
#S.C- O(1)

#Method 2

class RotatedMatrix:
    def __init__(self, square_matrix):
        self._square_matrix = square_matrix
    def read_entry(self, i, j):
        return self._square_matrix[~j][i]
    
    def write_entry(self, i, j, v):
        self._square_matrix[~j][i] = v
# T.C and S.C - O(1)
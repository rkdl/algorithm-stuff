####
# Python-specific solution (since all the elements of the list(s) are nullable)
# Also, we could make use of a fact that python implements arbitrary-precision arithmetic for ints
# Time: O(M * N), Mem: O(1)
# Where M = num of rows, N = num of columns
####

MARKED = {None, 0}

def mark_to_fill(matrix, i, j):
    for x in range(len(matrix)):
        if matrix[x][j] not in MARKED:
            matrix[x][j] = None
    for y in range(len(matrix[0])):
        if matrix[i][y] not in MARKED:
            matrix[i][y] = None


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    mark_to_fill(matrix, i, j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] is None:
                    matrix[i][j] = 0


########
# Solution 2 (supposed to be canonic, uh-huh)
# Time: O(M * N), Mem: O(1)
# Use first row and a first column in a special way -- storing 0 here 
# means the complete row/column should me marked 0 in the second pass
########
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_len = len(matrix)
        cols_len = len(matrix[0])
        
        should_zero_first_column = False

        for i in range(rows_len):
            if matrix[i][0] == 0:
                should_zero_first_column = True

            for j in range(1, cols_len):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rows_len):
            for j in range(1, cols_len):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(cols_len):
                matrix[0][j] = 0
        
        if should_zero_first_column:
            for i in range(rows_len):
                matrix[i][0] = 0

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        
        for k in range(size // 2):
            for i in range((size + 1) // 2):
                matrix[i][-1-k], prev = matrix[k][i], matrix[i][-1-k]
                matrix[-1-k][-1-i], prev = prev, matrix[-1-k][-1-i]
                matrix[-1-i][k], prev = prev, matrix[-1-i][k]
                matrix[k][i] = prev

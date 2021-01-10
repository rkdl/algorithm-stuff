class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        path = []
        upper_bound = 0
        lower_bound = len(matrix) - 1
        left_bound = 0
        right_bound = len(matrix[0]) - 1
        exp_size = len(matrix) * len(matrix[0])
        while len(path) < exp_size:
            for j in range(left_bound, right_bound + 1):
                path.append(matrix[upper_bound][j])
            upper_bound += 1
            for i in range(upper_bound, lower_bound + 1):
                path.append(matrix[i][right_bound])
            right_bound -= 1
            for j in range(right_bound, left_bound - 1, -1):
                path.append(matrix[lower_bound][j])
            lower_bound -= 1
            print(f'{lower_bound=}')
            for i in range(lower_bound, upper_bound - 1, -1):
                path.append(matrix[i][left_bound])
            left_bound += 1
            print(f'{path=}')
        return path

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        path = []
        if not matrix or not matrix[0]:
            return path

        position_offsets = ((0, 1), (1, 0), (0, -1), (-1, 0))
        steps_left = [len(matrix[0]), len(matrix) - 1]

        row = 0
        col = -1
        position_idx = 0
        while steps_left[position_idx % 2] > 0:
            offset_row, offset_col = position_offsets[position_idx]
            for _ in range(steps_left[position_idx % 2]):
                row += offset_row
                col += offset_col
                path.append(matrix[row][col])
            steps_left[position_idx % 2] -= 1
            position_idx = (position_idx + 1) % 4

        return path

class Solution:
    def traverse_island(self, grid: List[List[int]], i: int, j: int) -> int:
        stack = [
            (i, j),
        ]
        area = 0
        
        while stack:
            i, j = stack.pop()
            if (
                0 <= i < len(grid) and
                0 <= j < len(grid[i]) and
                grid[i][j] == 1
            ):
                grid[i][j] = -1
                area += 1
                stack.append((i - 1, j))
                stack.append((i, j + 1))
                stack.append((i + 1, j))
                stack.append((i, j - 1))
        
        return area
                

                
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        traverse_island = self.traverse_island
        
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    max_area = max(max_area, traverse_island(grid, i, j))
        
        return max_area


"""
Time complexity: O(N) where N = numOfRows * numOfColumns
Memory complexity: O(maxDepth) where maxDepth = max(numOfRows, numOfColumns)
"""

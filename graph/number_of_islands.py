def traverse_island(grid, visited, i, j):
    stack = [
        (i, j),
    ]
    while stack:
        i, j = stack.pop()
        if (
            0 <= i < len(grid)
            and 0 <= j < len(grid[i])
            and grid[i][j] == '1'
            and not visited[i][j]
        ):
            visited[i][j] = True
            stack.append((i + 1, j))
            stack.append((i, j + 1))
            stack.append((i - 1, j))
            stack.append((i, j - 1))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = [
            [False for _ in range(len(grid[i]))]
            for i in range(len(grid))
        ]

        islands_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and not visited[i][j]:
                    traverse_island(grid, visited, i, j)
                    islands_count += 1

        return islands_count

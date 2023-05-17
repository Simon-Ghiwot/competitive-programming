class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            total = 1
            grid[row][col] = 0
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in dir:
                total += dfs(grid, d[0] + row, d[1] + col)
            return total
        max_ = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_ = max(max_, dfs(grid, i, j))
        return max_

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(grid, row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in dir:
                dfs(grid, d[0] + row, d[1] + col)
            return 
        total = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    total += 1
                    dfs(isConnected, i, j)
        return total

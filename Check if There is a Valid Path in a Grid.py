class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {1 : [[0, 1], [0, -1]], 2 : [[1, 0], [-1, 0]],
                      3: [[0, -1], [1, 0]], 4 : [[0, 1], [1, 0]],
                      5: [[-1, 0], [0, -1]], 6 : [[-1, 0], [0, 1]]}
        ROW, COL = len(grid), len(grid[0])
        visited = [[False] * COL for i in range(ROW)]
        combinations = {(1, 0) : [1, 3, 5], (1, 1) : [1, 4, 6],
                        (2, 0) : [2, 5, 6], (2, 1) : [2, 4, 3],
                        (3, 0) : [1, 4, 6], (3, 1) : [2, 5, 6],
                        (4, 0) : [1, 3, 5], (4, 1) : [2, 5, 6],
                        (5, 0) : [2, 3, 4], (5, 1) : [1, 4, 6],
                        (6, 0) : [2, 3, 4], (6, 1) : [1, 3, 5]}

        def dfs(row, col, visited):
            if row == ROW - 1 and col == COL - 1:
                return True
            visited[row][col] = True
            for i in range(len(directions[grid[row][col]])):
                x, y = directions[grid[row][col]][i]
                n_r, n_c = row + x, col + y
                if n_r < 0 or n_r >= ROW or n_c < 0 or n_c >= COL or visited[n_r][n_c]:
                    continue
                next, cur = grid[n_r][n_c], grid[row][col]
                if next not in combinations[(cur, i)]:
                    continue
                if dfs(n_r, n_c, visited):
                    return True
            return False
        return dfs(0, 0, visited)

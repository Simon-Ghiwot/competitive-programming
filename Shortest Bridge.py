class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def is_valid(r, c, visited):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or visited[r][c] or grid[r][c] == 0:
                return False
            return True
        def is_valid_bfs(r, c, visited):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or visited[r][c]:
                return False
            return True
        def dfs(que, r, c, visited):
            if not is_valid(r, c, visited):
                return
            visited[r][c] = True
            que.append((r, c))
            for x, y in dir:
                n_r, n_c = x + r, y + c
                dfs(que, n_r, n_c, visited)
        
        found = False
        que = deque()
        visited = [[False] * len(grid[0]) for _ in range(len(grid))] 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(que, i, j, visited)
                    found = True
                    break

            if found:  
                break
        ans = 0
        while que:
            for i in range(len(que)):
                row, col = que.popleft()
                for x, y in dir:
                    n_r, n_c = row + x, col + y
                    if not is_valid_bfs(n_r, n_c, visited):
                        continue
                    if grid[n_r][n_c] == 1:
                        return ans
                    que.append((n_r, n_c))
                    visited[n_r][n_c] = True
            ans += 1
        return 0

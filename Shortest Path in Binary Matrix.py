class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]

        def is_valid(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or visited[i][j] or grid[i][j] == 1:
                return False
            return True

        visited = [[False for j in i] for i in grid]
        nodes, que, ok = -1, deque(), False
        que.append((0, 0, 1))
        visited[0][0] = True
        while que:
            for i in range(len(que)):
                row, col, prev = que.popleft()
                if row == len(grid) - 1 and col == len(grid) - 1:
                    ok = True
                    nodes = prev
                    break
                for d in dir:
                    r, c = row + d[0], col + d[1]
                    if is_valid(r, c):
                        visited[r][c] = True
                        que.append((r, c, prev + 1))
        
        return nodes

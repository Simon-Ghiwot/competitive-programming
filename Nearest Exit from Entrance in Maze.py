class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False] * len(maze[0]) for _ in range(len(maze))] 
        que = deque()
        time = 0
        que.append((entrance[0], entrance[1]))
        visited[entrance[0]][entrance[1]] = True
        while que:
            for i in range(len(que)):
                r, c = que.popleft()
                if r == len(maze) - 1 or c == len(maze[0]) - 1 or r == 0 or c == 0:
                    if r != entrance[0] or c != entrance[1]:
                        return time
                for x, y in dir:
                    n_r, n_c = x + r, y + c
                    if n_r < 0 or n_c < 0 or n_r >= len(maze) or n_c >= len(maze[0]) or visited[n_r][n_c]:
                        continue
                    if maze[n_r][n_c] == '+':
                        continue
                    visited[n_r][n_c] = True
                    que.append((n_r, n_c))
            time += 1
        return -1

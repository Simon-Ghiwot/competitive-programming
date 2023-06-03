class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = [[False] * len(mat[0]) for _ in range(len(mat))] 
        ans = [[0] * len(mat[0]) for _ in range(len(mat))]
        que = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited[i][j] = True
                    que.append((i, j, 0))
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while que:
            r, c, d = que.popleft()
            ans[r][c] = d
            for x, y in dir:
                n_r, n_c = r + x, c + y
                if n_r < 0 or n_c < 0 or n_r >= len(mat) or n_c >= len(mat[0]) or visited[n_r][n_c]:
                    continue
                que.append((n_r, n_c, d + 1))
                visited[n_r][n_c] = True


        return ans

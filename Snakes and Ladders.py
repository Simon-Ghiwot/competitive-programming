class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        cell_num = defaultdict(int)
        num, dir = 1, True
        last_cell = len(board) ** 2
        for i in range(len(board) - 1, -1, -1):
            if dir:
                for j in range(len(board)):
                    cell_num[num] = (i, j)
                    num += 1
            else:
                for j in range(len(board) - 1, -1, -1):
                    cell_num[num] = (i, j)
                    num += 1
            dir ^= 1
        visited = [False] * (last_cell + 1)
        que = deque()
        que.append((1, 0))
        visited[1] = True
        while que:
            at, res = que.popleft()
            if at == last_cell:
                return res
            for to in range(at + 1, min(at + 6, last_cell) + 1):
                
                r, c = cell_num[to]
                if board[r][c] != -1:
                    to = board[r][c]
                    r, c = cell_num[to]
                if visited[to]: continue
                visited[to] = True
                que.append((to, res + 1))
        return -1

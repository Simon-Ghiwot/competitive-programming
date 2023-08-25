class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        que = deque()
        que.append((click[0], click[1]))
        visited = set()
        visited.add((click[0], click[1]))
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        while que:
            r, c = que.popleft()
            mines, childs = 0, []
            for x, y in dir:
                nr, nc = x + r, y + c
                if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]) or (nr, nc) in visited:
                    continue
                if board[nr][nc] == 'M':
                    mines += 1
                else:
                    if (nr, nc) not in visited:
                        childs.append((nr, nc))
            if mines == 0:
                board[r][c] = 'B'
                for x, y in childs:
                    que.append((x, y))
                    visited.add((x, y))
            else:
                board[r][c] = str(mines)
        return board

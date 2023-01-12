class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x, o = 0, 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    x += 1
                elif board[i][j] == 'O':
                    o += 1
        if o > x or x - o > 1:
            return False
        # one person finished first
        def hasWinner(board, symbol):
            column, diagonal = [], []
            posD, negD = [], []
            for i in range(3):
                col = []
                for j in range(3):
                    col.append(board[j][i])
                    if i == j:
                        negD.append(board[i][j])
                    if i + j == 2:
                        posD.append(board[i][j])
                column.append("".join(col))
            diagonal.append("".join(posD))
            diagonal.append("".join(negD))
            if symbol == "X":
                if board[0] == "XXX" or board[1] == "XXX" or board[2] == "XXX":
                    return True
                if column[0] == "XXX" or column[1] == "XXX" or column[2] == "XXX":
                    return True
                if diagonal[0] == "XXX" or diagonal[1] == "XXX":
                    return True
            else:
                if board[0] == "OOO" or board[1] == "OOO" or board[2] == "OOO":
                    return True
                if column[0] == "OOO" or column[1] == "OOO" or column[2] == "OOO":
                    return True
                if diagonal[0] == "OOO" or diagonal[1] == "OOO":
                    return True
            return False
        if hasWinner(board, 'X') and o == x or hasWinner(board, 'O') and x > o:
            return False 
        
        return True

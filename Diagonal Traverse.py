class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        row, col, total = 0, 0, len(mat) * len(mat[0])
        direction = True
        for i in range(total):
            result.append(mat[row][col])
            print(row, col)
            if row == 0 and direction and col == len(mat[0]) - 1:
                row += 1
                direction = not direction
            elif col == 0 and not direction and row == len(mat) - 1:
                col += 1
                direction = not direction
            elif row == 0 and direction or row == len(mat) - 1 and not direction:
                col += 1
                direction = not direction
            elif col == 0 and not direction or col == len(mat[0]) - 1 and direction:
                row += 1
                direction = not direction
            elif direction:
                row -= 1
                col += 1
            else:
                row += 1
                col -= 1
            
        return result
    # if am at top or bottom coner change col
    # if am at left or right corner change row
    # took about 20 minutes

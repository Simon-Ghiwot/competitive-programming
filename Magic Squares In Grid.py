class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if(len(grid) < 3 or len(grid[0]) < 3):
            return 0
        
        def is_magic_square(row, col):
            visited = set()
            for r in range(row, row - 3, -1):
                for c in range(col, col - 3, -1):
                    if grid[r][c] in visited or grid[r][c] > 9 or grid[r][c] < 1:
                        return 0
                    else:
                        visited.add(grid[r][c])
            total = []
            for r in range(row, row - 3, -1):
                total.append(sum(grid[r][col - 2 : col + 1]))

            for c in range(col, col - 3, -1):
                cur = 0
                for r in range(row, row - 3, -1):
                    cur += grid[r][c]
                total.append(cur)
            negDig = grid[row][col] + grid[row - 1][col - 1] + grid[row - 2][col - 2]
            posDig = grid[row][col - 2] + grid[row - 1][col - 1] + grid[row - 2][col]
            total.append(negDig)
            total.append(posDig)

            for i in total:
                if i != posDig:
                    return 0
            return 1 


        result = 0
        for i in range(2, len(grid)):
            for j in range(2, len(grid[0])):
                result += is_magic_square(i, j)
        
        return result

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        zeroRow = [0 for i in range(len(grid))]
        oneRow = [0 for i in range(len(grid))]
        zeroCol = [0 for i in range(len(grid[0]))]
        oneCol = [0 for i in range(len(grid[0]))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    zeroCol[j] += 1
                    zeroRow[i] += 1
                else:
                    oneCol[j] += 1
                    oneRow[i] += 1
        result = []
        for i in range(len(grid)):
            cur = []
            for j in range(len(grid[0])):
                cur.append(oneRow[i] + oneCol[j] - zeroRow[i] - zeroCol[j])
            result.append(cur)
        return result
# took about 13 minutes

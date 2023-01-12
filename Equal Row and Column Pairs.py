class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pair = {}
        for i in range(len(grid)):
            row = " ".join(map(str, grid[i]))
            pair[row] = pair.get(row, 0) + 1
        
        result = 0
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(str(grid[j][i]))
            col = " ".join(col)
            if pair.get(col):
                result += pair[col]

        return result

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = [[0 for j in range(len(grid) -2) ] for i in range(len(grid) - 2)]


        def find_max(i, j):
            _max = 0
            for x in range(i, i - 3, -1):
                for y in range(j, j - 3, -1):
                    _max = max(_max, grid[x][y])
            return _max

        for i in range(2, len(grid)):
            for j in range(2, len(grid)):
                result[i - 2][j - 2] = find_max(i, j)

        return result

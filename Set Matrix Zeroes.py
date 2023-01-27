class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = [0 for i in range(len(matrix))]
        col = [0 for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] += 1
                    col[j] += 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] > 0 or col[j] > 0:
                    matrix[i][j] = 0

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ROW, COL = len(mat), len(mat[0])
        if ROW * COL != r * c:
            return mat

        combined = []
        for i in range(ROW):
            for j in range(COL):
                combined.append(mat[i][j])
        result = [[0 for j in range(c)] for i in range(r)]

        for i in range(len(combined)):
            row = i // c
            col = i % c
            result[row][col] = combined[i]
        return result

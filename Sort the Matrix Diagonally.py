class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat) - 1, 0
        result = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
        while col < len(mat[0]):
            cur = []
            temp_row, temp_col = row, col

            # getting the elements to sort
            while temp_row < len(mat) and temp_col < len(mat[0]):
                cur.append(mat[temp_row][temp_col])
                # print(temp_row, temp_col)
                temp_row += 1
                temp_col += 1

            cur.sort()

            # filling the output array
            temp_row, temp_col, i = row, col, 0
            while temp_row < len(mat) and temp_col < len(mat[0]):
                result[temp_row][temp_col] = cur[i]
                temp_row += 1
                temp_col += 1
                i += 1
            if row != 0:
                row -= 1
            else:
                col += 1
        return result

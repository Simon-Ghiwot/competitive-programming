class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        pref = [[0] * (len(mat[0]) + 1) for i in range(len(mat) + 1)]
        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                pref[i][j] = mat[i - 1][j - 1] + pref[i][j - 1] + pref[i - 1][j] - pref[i - 1][j - 1]

        ans = [[0] * len(mat[0]) for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):

                r = i + k + 1 if i + k + 1 < len(pref) else len(pref) - 1
                c = j + k + 1 if j + k + 1 < len(pref[0]) else len(pref[0]) - 1
                ans[i][j] += pref[r][c]

                c = j - k if j - k >= 0 else 0
                ans[i][j] -= pref[r][c]

                r = i - k if i - k >= 0 else 0
                c = j + k + 1 if j + k + 1 < len(pref[0]) else len(pref[0]) - 1
                ans[i][j] -= pref[r][c]

                c = j - k if j - k >= 0 else 0
                ans[i][j] += pref[r][c]

        return ans
        

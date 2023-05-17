class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image, ans, visited, row, col, original, new):
            if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]):
                return
            if (row, col) in visited or image[row][col] != original:
                return
            
            visited.add((row, col))
            ans[row][col] = new
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in dir:
                dfs(image, ans, visited, row + d[0], col + d[1], original, new)

        ans = []
        for row in image:
            ans.append(row[:])
        dfs(image, ans, set(), sr, sc, image[sr][sc], color)
        return ans
        

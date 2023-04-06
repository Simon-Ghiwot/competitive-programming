class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.backtrack(1, n, k, [])
        return self.ans
    def backtrack(self,start, n, k, current):
        if len(current) == k:
            self.ans.append(current[:])
            return
        for i in range(start, n + 1):
            current.append(i)
            self.backtrack(i + 1, n, k, current)
            current.pop()

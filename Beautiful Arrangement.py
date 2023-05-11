class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        self.visited = [False] * (n + 1)
        self.backtrack(n, 1, [])
        return self.ans
    def backtrack(self, n, index, cur):
        if len(cur) == n:
            self.ans += 1
            return
        for i in range(1, n + 1):
            if self.visited[i] or (index % i != 0 and i % index != 0):
                continue
            self.visited[i] = True
            cur.append(index)
            self.backtrack(n, index + 1, cur)
            self.visited[i] = False
            cur.pop()
        

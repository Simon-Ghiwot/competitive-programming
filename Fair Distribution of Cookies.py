class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if len(cookies) == k: # otherwise it TLE
            return max(cookies)
        self.ans = 10e6 + 600
        children = [0] * k
        self.backtrack(cookies, children, 0)
        return self.ans

    def backtrack(self, cookies, children, index):
        if index == len(cookies):
            self.ans = min(self.ans, max(children))
            return
        for i in range(len(children)):
            children[i] += cookies[index]
            self.backtrack(cookies, children, index + 1)
            children[i] -= cookies[index]
        

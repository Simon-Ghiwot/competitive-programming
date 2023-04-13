# problem exactly same approach as https://leetcode.com/problems/palindrome-partitioning/description/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ans = []
        store = set(wordDict)
        self.backtrack(s, store, 0, [])
        return self.ans
    def backtrack(self, s, store, start, current):
        if start == len(s):
            self.ans.append(" ".join(current))
            return
        for i in range(start, len(s)):
            if s[start : i + 1] not in store:
                continue
            
            current.append(s[start : i + 1])
            self.backtrack(s, store, i + 1, current)
            current.pop()

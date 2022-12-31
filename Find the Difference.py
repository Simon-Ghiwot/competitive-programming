class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_set = set()
        for c in s:
            s_set.add(c)
        for c in t:
            if c not in s_set:
                return c 
        return '\0'

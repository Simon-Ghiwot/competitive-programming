class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_map, t_map = {}, {}
        for c in s:
            s_map[c] = s_map.get(c, 0) + 1
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1

        for c in t:
            if c not in  s_map:
                return c 
            if s_map.get(c) != t_map.get(c):
                return c
        return '\0'

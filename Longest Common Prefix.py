class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

class Solution:
    def convertToTitle(self, val: int) -> str:
        ans = []
        while val:
            val -= 1
            cur = val % 26
            ans.append(chr(cur + 65))
            val = val // 26
        return "".join(ans)[::-1]

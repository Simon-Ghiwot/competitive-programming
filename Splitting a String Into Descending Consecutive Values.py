class Solution:
    def splitString(self, s: str) -> bool:

        return self.backtrack(s, 0, -1, False, [])

    def backtrack(self, s, start, prev_num, first, previous):
        if start == len(s):
            return True if len(previous) > 1 else False

        for i in range(start, len(s)):
            cur_num = int(s[start : i + 1])
            
            if first and prev_num - cur_num != 1:
                    continue
            previous.append(cur_num)
            if self.backtrack(s, i + 1, cur_num, True, previous):
                return True
            previous.pop()

        return False

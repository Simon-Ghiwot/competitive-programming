class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return self.backtrack(num, 0, [])
    def backtrack(self, num, start, cur):
        if len(cur) >= 3:
            if cur[-2] + cur[-3] != cur[-1]:
                return False
            
        if start == len(num):
            return True if len(cur) > 2 else False

        for i in range(start, len(num)):
            cur_num = int(num[start : i + 1])
            cur.append(cur_num)
            if self.backtrack(num, i + 1, cur):
                return True
            cur.pop()
            if cur_num == 0:
                break
        return False
        

class Solution:
    def findComplement(self, num: int) -> int:
        last_bit = ceil(log2(num))
        ans = 0
        for bit in range(last_bit):
            if not num & (1 << bit):
                ans |= (1 << bit)
        return ans

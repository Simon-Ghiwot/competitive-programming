class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # just use bitmasking and compare the two numbers
        ans = 0
        for i in range(31):
            if x & (1 << i) != y & (1 << i):
                ans += 1
        return ans

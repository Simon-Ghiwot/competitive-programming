class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        neg = 0
        for num in nums:
            if num < 0:
                neg += 1
        
        ans, freq = 0, [0] * 31
        for num in nums:
            for bit in range(31):
                if num & (1 << bit):
                    freq[bit] += 1
        
        for bit in range(31):
            if freq[bit] % 3 == 1:
                ans = ans | (1 << bit)

        return ans if not neg % 3 else -1 * (pow(2, 31) - ans)

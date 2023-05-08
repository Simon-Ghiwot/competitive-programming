class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # use the fact that or function is always increasing
        # thus the maximum number is always going to be the whole array
        ans = max_ = 0
        for num in nums:
            max_ |= num

        for i in range(pow(2, len(nums))):
            cur = 0
            for bit in range(31):
                if i & (1 << bit) != 0:
                    cur |= nums[bit]
            if cur == max_:
                ans += 1
        return ans

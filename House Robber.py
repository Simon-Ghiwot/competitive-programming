class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            cur = nums[i - 1]
            if i != 1:
                cur += dp[i - 2]
            dp[i] = max(dp[i  - 1], cur)
        return dp[len(nums)]

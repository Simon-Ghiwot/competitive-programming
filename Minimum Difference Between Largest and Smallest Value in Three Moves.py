class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        ans = min(nums[-4] - nums[0], nums[-1] - nums[3])
        ans2 = min(nums[-2] - nums[2], nums[-3] - nums[1])
        return min(ans, ans2)

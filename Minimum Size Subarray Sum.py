class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if(sum(nums) < target):
            return 0
        total = 0
        min_ = 100001
        left = right = 0
        while right < len(nums):
            total += nums[right]
            while total >= target:
                min_ = min(min_, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return min_

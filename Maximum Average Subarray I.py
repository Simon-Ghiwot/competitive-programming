class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ = 0
        for i in range(k):
            max_ += nums[i]
        running_sum = max_
        for i in range(0, len(nums) - k):
            running_sum -= nums[i]
            running_sum += nums[i + k]
            max_ = max(max_, running_sum)
        return max_ / k
        

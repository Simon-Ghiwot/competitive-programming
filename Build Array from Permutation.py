class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            result[i] = nums[nums[i]]
        return result

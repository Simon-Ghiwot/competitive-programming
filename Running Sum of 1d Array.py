class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            total = nums[i] + (0 if not result else result[-1])
            result.append(total)

        return result

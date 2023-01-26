class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] > nums[j]:
                    count += 1
            result[i] = count
        return result

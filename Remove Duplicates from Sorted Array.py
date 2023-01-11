class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pivot = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                pivot += 1
                nums[pivot] = nums[i]
        return pivot + 1

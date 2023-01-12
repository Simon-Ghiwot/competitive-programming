class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postive, negative = 0, 1
        while negative < len(nums):
            while postive < len(nums) and nums[postive] > 0:
                postive += 2
            while negative < len(nums) and nums[negative] < 0:
                negative += 2
            if negative < len(nums):
                nums[postive], nums[negative] = nums[negative], nums[postive]
        return nums

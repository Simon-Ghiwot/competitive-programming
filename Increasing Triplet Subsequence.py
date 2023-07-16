class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        INF = 10e9
        one = two = INF
        for i in range(len(nums)):
            if nums[i] > two:
                return True
            elif nums[i] < two and nums[i] > one:
                two = nums[i]
            elif nums[i] < one:
                one = nums[i]

        return False

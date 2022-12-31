class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        map = {}
        result = 0
        for i in range(len(nums)):
            if map.get(nums[i]):
                result += map.get(nums[i], 0)
            if map.get(nums[i]):
                map[nums[i]] += 1
            else:
                map[nums[i]] = 1
        return result

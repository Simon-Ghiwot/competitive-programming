class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        total = 0
        for i in nums:
            if i % 2 == 0:
                total += i
            
        for val, index in queries:
            if nums[index] % 2 == 0 and val % 2 == 0:
                total += val
            elif nums[index] % 2 == 1 and val % 2 == 1:
                total += nums[index] + val
            elif nums[index] % 2 == 0 and val % 2 == 1:
                total -= nums[index]
            nums[index] += val
            result.append(total)
        return result
# i don't know how much time it took probably around 15

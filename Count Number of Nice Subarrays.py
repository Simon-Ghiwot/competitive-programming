class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = (0 if nums[i] % 2 == 0 else 1)
        count = defaultdict(int)
        count[0] += 1
        running_sum = result = 0

        for i in range(len(nums)):
            running_sum += nums[i]
            result += count[running_sum - k]
            count[running_sum] += 1

        return result

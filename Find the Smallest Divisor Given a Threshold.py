class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, 10e9
        def find_total(divisor):
            total = 0
            for num in nums:
                total += (num + divisor - 1) // divisor
            return total

        while left <= right:
            mid = (left + right) // 2
            sum_ = find_total(mid)

            if sum_ > threshold:
                left = mid + 1
            else:
                right = mid - 1
        
        return int(left)

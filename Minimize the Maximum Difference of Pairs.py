class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def ok(mid):
            ans = []
            i, pair = 1, 0
            while i < len(nums) and pair < p: 
                if nums[i] - nums[i - 1] <= mid:
                    pair += 1
                    i += 1
                i += 1
            
            return pair >= p

        left, right, ans = 0, max(nums), 0
        while left <= right:
            mid = (left + right) // 2
            if ok(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return int(ans)

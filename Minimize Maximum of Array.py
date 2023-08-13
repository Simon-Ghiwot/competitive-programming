class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def ok(mid):
            t_num = nums[:]
            for i in range(len(nums) - 1, 0, -1):
                if t_num[i] > mid:
                    t_num[i - 1] += t_num[i] - mid
                    t_num[i] = mid
            return max(t_num) <= mid
        
        left, right, ans = 0, max(nums), 0
        
        while left <= right:
            mid = (left + right) // 2
            if ok(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
        

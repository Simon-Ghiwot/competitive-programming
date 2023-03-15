class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def find_winner(l, r):
            if l == r:
                return nums[l]
            chose_l = nums[l] - find_winner(l + 1, r)
            chose_r = nums[r] - find_winner(l, r - 1)

            return max(chose_l, chose_r)
        
        return True if find_winner(0, len(nums) - 1) >= 0 else False

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # proof the xor of a ^ a is 0
        # the identity number for xor is 0
        # thus when we find a number twice the xor becomes zero
        # final when we find the single number ans xor w zero 
        # it will remain the same
        ans = 0
        for num in nums:
            ans ^= num
        return ans

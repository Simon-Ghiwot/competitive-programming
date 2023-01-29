class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left, right = 0, len(piles) - 1

        result = 0
        while left < right:
            result += piles[right - 1]
            right -= 2
            left += 1
 
        return result

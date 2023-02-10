class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # check if perfect square
        root = int(sqrt(c))
        if root ** 2 == c:
            return True
        left, right = 0, int(sqrt(c)) + 1
        while left <= right:
            sum = left ** 2 + right ** 2
            if sum == c:
                return True
            if sum > c:
                right -= 1
            else:
                left += 1
        return False
        

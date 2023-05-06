class Solution:
    def countPrimes(self, n: int) -> int:
        ans = 0
        is_prime = [True] * n
        i = 2
        while i < n:
            if is_prime[i]:
                j = i * i
                ans += 1
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1
        return ans

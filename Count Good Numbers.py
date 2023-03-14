class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        def myPow(x, n):
            if n == 0:
                return 1
            if n % 2:
                return x % mod * myPow(x, n - 1) % mod
            return myPow((x % mod * x % mod) % mod, n / 2)
        
        odd = myPow(4, n// 2) % mod
        even = myPow(5, (n + 1) // 2) % mod

        return (odd % mod * even % mod) % mod

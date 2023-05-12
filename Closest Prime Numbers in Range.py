class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def seive(n, primes):
            is_prime = [True] * n
            i = 2
            while i < n:
                if is_prime[i]:
                    j = i * i
                    primes.append(i)
                    while j < n:
                        is_prime[j] = False
                        j += i
                i += 1

        primes = []
        seive(right + 1, primes)
        ans = 10e6 + 600
        ans_primes =[-1, -1]
        i = 0
        while i < len(primes) and primes[i] < left:
            i += 1
        for j in range(i, len(primes) - 1):
            if primes[j + 1] > right:
                break
            if ans > primes[j + 1] - primes[j]:
                ans = min(ans, primes[j + 1] - primes[j])
                ans_primes = [primes[j], primes[j + 1]]

        return ans_primes

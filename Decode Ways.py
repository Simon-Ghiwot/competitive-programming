class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * len(s)
        def backtrack(s, idx, memo):
            if idx == len(s):
                return 1
            if memo[idx] != -1:
                return memo[idx]
            ones = twos = 0
        
            if s[idx] != '0':
                ones = backtrack(s, idx + 1, memo)
                if idx + 1 < len(s) and int(s[idx : idx + 2]) <= 26:
                    twos = backtrack(s, idx + 2, memo)
            memo[idx] = ones + twos
            return memo[idx]

        return backtrack(s, 0, memo)

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        map = {}
        mod = 10**9 + 7
        result = 0
        for d in deliciousness:
            for i in range(22):
                result = (result % mod + map.get(2**i - d, 0) % mod) % mod
            if map.get(d):
                map[d] += 1
            else:
                map[d] = 1
        return result

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        max_ = 0
        for s, e in intervals:
            max_ = max(max_, e)
        res = [0] * (max_ + 1)

        for s, e in intervals:
            res[s - 1] += 1
            res[e] -= 1
        return max(accumulate(res))

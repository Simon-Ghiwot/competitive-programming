class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n, interval_with_index = len(intervals), []

        for i in range(n):
            interval_with_index.append([*intervals[i], i])
        interval_with_index.sort()
        result = [0] * n

        def search(end_interval, start_index):
            left, right = start_index, n - 1
            ans = 10**7

            while left <= right:
                mid = (left + right) // 2
                if interval_with_index[mid][0] < end_interval:
                    left = mid + 1
                else:
                    ans = interval_with_index[mid][2]
                    right = mid - 1
            return -1 if ans == 10**7 else ans

        for i in range(n):
            start, end, index = interval_with_index[i]
            result[index] = search(end, i)

        return result

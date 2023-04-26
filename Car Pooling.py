class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        line = [0] * 1001
        for seats, start, end in trips:
            line[start] += seats
            line[end] -= seats

        for i in range(1, len(line)):
            line[i] += line[i - 1]

        return max(line) <= capacity

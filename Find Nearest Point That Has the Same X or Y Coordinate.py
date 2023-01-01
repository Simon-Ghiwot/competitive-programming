class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minHeap = []
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                minHeap.append([abs(x - points[i][0]) + abs(y - points[i][1]), i])
                print("here")
        heapq.heapify(minHeap)
        return minHeap[0][1] if minHeap else -1

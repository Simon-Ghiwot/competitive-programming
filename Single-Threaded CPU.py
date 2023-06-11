# ugly code but there are nicer and shorter code than this
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ordered = [(enq, pro, i) for i, (enq, pro) in enumerate(tasks)]
        ordered.sort()

        i, heap, ans, time = 0, [], [], 0
        heapq.heapify(heap)

        def add_to_heap(heap, idx):
            start, processing, idx = ordered[idx]
            heapq.heappush(heap, [processing, idx, start])
        
        while i < len(tasks):
            while heap:
                process, idx, start = heapq.heappop(heap)
                time += process
                ans.append(idx)
                while i < len(tasks) and ordered[i][0] <= time:
                    add_to_heap(heap, i)
                    i += 1
            if not heap:
                cur = -1
                if i < len(tasks):
                    time += ordered[i][0]
                    cur = ordered[i][0]
                while i < len(tasks) and ordered[i][0] <= cur:
                    add_to_heap(heap, i)
                    i += 1
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        buckets = [[] for i in range(len(words) + 1)]
        for i in range(len(buckets)):
            heapq.heapify(buckets[i])
        for key in freq.keys():
            heapq.heappush(buckets[freq[key]], key)
        ans = []
        for i in range(len(words) - 1, -1, -1):
            while buckets[i]:
                if len(ans) == k:
                    return ans
                ans.append(heappop(buckets[i]))
        return ans
            

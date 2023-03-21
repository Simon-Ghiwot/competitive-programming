class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        word_freq = []
        for i in range(len(words)):
            temp = [s for s in words[i]]
            temp.sort()
            count = Counter(temp)
            word_freq.append(count[temp[0]])
        word_freq.sort()
        def search(target):
            left, right = 0, len(words) - 1
            while left <= right:
                mid = (left + right) // 2
                if target >= word_freq[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return len(words) - left

        result = []
        for q in queries:
            temp = [s for s in q]
            temp.sort()
            count = Counter(temp)
            target = count[temp[0]]
            result.append(search(target))

        return result

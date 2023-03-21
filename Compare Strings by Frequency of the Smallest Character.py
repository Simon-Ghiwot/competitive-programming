class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        word_freq = []
        def find_min_count(word):
            temp = [s for s in word]
            temp.sort()
            count = Counter(temp)
            return count[temp[0]]

        for i in range(len(words)):
            word_freq.append(find_min_count(words[i]))
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
            result.append(search(find_min_count(q)))

        return result

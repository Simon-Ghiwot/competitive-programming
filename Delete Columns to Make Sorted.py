class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        result = 0
        for i in range(len(strs[0])):
            current = [strs[0][i]]
            for j in range(1, len(strs)):
                if current[j - 1] > strs[j][i]:
                    result += 1
                    break
                current.append(strs[j][i])
                
        return result

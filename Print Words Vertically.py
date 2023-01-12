class Solution:
    def printVertically(self, s: str) -> List[str]:
        word = s.split(' ');
        result = []
        maxLen = 0
        for i in range(len(word)):
            maxLen = max(maxLen, len(word[i]))
        for i in range(maxLen):
            curr = []
            for j in range(len(word)):
                if i < len(word[j]):
                    curr.append(word[j][i])
                else:
                    curr.append(" ")
            while curr[-1] == " ":
                curr.pop()
                print("here")
            result.append("".join(curr))
        return result

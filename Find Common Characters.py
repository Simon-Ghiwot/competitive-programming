class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters = [0] * 26

        offset = ord('a')

        for letter in words[0]:
            letters[ord(letter) - offset] += 1

        for i in range(1, len(words)):
            temp = [0] * 26
            for letter in words[i]:
                temp[ord(letter) - offset] += 1

            for j in range(0, 26):
                letters[j] = min(letters[j], temp[j])
                

        result = []
        for i in range(0, 26):
            if letters[i] != 0:
                result.extend([chr(i + offset)] * letters[i])
        
        return result
        

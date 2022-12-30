class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}
        for i in range(len(order)):
            alphabet[order[i]] = i 
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(len(word1)):
                if j >= len(word2) or alphabet[word1[j]] > alphabet[word2[j]]:
                    return False
                if alphabet[word1[j]] < alphabet[word2[j]]:
                    break
        return True
        

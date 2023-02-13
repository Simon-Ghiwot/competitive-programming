class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        top = bottom = 0
        merged = []
        while top < len(word1) and bottom < len(word2):
            if word1[top] == word2[bottom]:
                if word1[top :] > word2[bottom :]:
                    merged.append(word1[top])
                    top += 1
                else:
                    merged.append(word2[bottom])
                    bottom += 1
            elif word1[top] > word2[bottom]:
                merged.append(word1[top])
                top += 1
            else:
                merged.append(word2[bottom])
                bottom += 1
        merged.extend(word1[top :])
        merged.extend(word2[bottom :])
        
        return "".join(map(str, merged))

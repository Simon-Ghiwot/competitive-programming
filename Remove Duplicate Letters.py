class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack, seen = [], set()
        freq = Counter(s)
        
        for letter in s:
            freq[letter] -= 1
            if letter not in seen:
                while stack and stack[-1] > letter and freq[stack[-1]] > 0:
                    seen.remove(stack[-1])
                    stack.pop()

                stack.append(letter)
                seen.add(letter)
        
        return "".join(stack)

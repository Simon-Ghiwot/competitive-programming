class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            else:
                total = 0
                while stack and stack[-1] != "(":
                    total += int(stack.pop())

                if total == 0:
                    total += 1
                else:
                    total *= 2
                stack.pop()
                stack.append(str(total))

        return sum(map(int, stack))

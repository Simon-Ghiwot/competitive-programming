class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        stack = []
        for i in range(len(command)):
            if command[i] == ')':
                temp = ""
                while stack and stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                temp = temp[::-1]
                if temp == "":
                    result += 'o'
                else:
                    result += "al"
            elif command[i] == "G":
                result += "G"
            else:
                stack.append(command[i])

        return result

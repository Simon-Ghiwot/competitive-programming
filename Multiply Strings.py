class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        resultBase = 1
        for current in num1[::-1]:
            curResult, carry = 0, 0
            current = int(current)
            base = 1

            for j in num2[::-1]:
                product = (current * int(j)+ carry) % 10
                curResult += product * base
                carry = (current * int(j) + carry) // 10
                base *= 10

            curResult += carry * base
            result += curResult * resultBase
            resultBase *= 10
            
        return str(result)

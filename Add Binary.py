class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        if len(b) != len(a):
            pad = ["0"] * abs(len(a) - len(b))
            pad = "".join(pad)
            if len(b) < len(a):
                b = pad + b
            else:
                a = pad + a

        carry = 0
        for i in range(len(b) - 1, -1, -1):
            sum_ = int(b[i]) + int(a[i]) + carry
            ans += str(sum_ % 2)
            carry = sum_ // 2

        if carry:
            ans += str(carry)

        return ans[::-1]

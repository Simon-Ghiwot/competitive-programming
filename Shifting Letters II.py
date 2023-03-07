class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s_ord = [ord(i) for i in s]
        final = [0] * (len(s) + 1)

        for shift in shifts:
            if shift[2] == 1:
                final[shift[0]] += 1
                final[shift[1] + 1] -= 1
            else:
                final[shift[0]] -= 1
                final[shift[1] + 1] += 1

        result = []
        for i in range(1, len(final)):
            final[i] += final[i - 1]
        for i in range(len(final) - 1):
            char = (s_ord[i] + final[i] - 97 + 26) % 26 + 97
            result.append(chr(char))

        return "".join(result)

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s_ord = [ord(i) for i in s]
        line = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            if direction == 1:
                line[start] += 1
                line[end + 1] -= 1
            else:
                line[start] -= 1
                line[end + 1] += 1

        result = []
        for i in range(1, len(line)):
            line[i] += line[i - 1]
        for i in range(len(line) - 1):
            char = (s_ord[i] + line[i] - 97 + 26) % 26 + 97
            result.append(chr(char))

        return "".join(result)

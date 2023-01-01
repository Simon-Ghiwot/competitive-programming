class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        result = ""
        while i >= 0:
            if(s[i] == '#'):
                result += chr(int(s[i - 2 : i]) + 96)
                # print(chr(int(s[i - 2 : i]) + 96))
                i -= 2
            else:
                result += chr(int(s[i : i + 1]) + 96)
                # print(chr(int(s[i : i + 1]) + 96))
            i -= 1
        return result[::-1]

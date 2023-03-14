class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        result = "0"
        def helper(string):
            list_string = [int(s) for s in string]
            for i in range(len(list_string)):
                list_string[i] ^= 1
            
            return "".join(map(str, list_string))
            
        result = ["0"]
        for i in range(n - 1):
            result.append(result[-1] + "1" + helper(result[-1])[::-1])

        return result[-1][k - 1]

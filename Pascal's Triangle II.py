class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]]
        def build(index):
            if index - 1 == rowIndex:
                return
            cur = [1]
            for i in range(len(result[-1]) - 1):
                cur.append(result[-1][i] + result[-1][i + 1])
            cur.append(1)
            result.append(cur[:])
            build(index + 1)

        build(1)
        return result[-1]

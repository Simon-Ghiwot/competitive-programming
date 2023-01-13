class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = [0, 0], [len(matrix) - 1, len(matrix[0]) - 1]
        result = []
        i = 0
        total = len(matrix) * len(matrix[0])

        while len(result) < total:
            # left to right
            for j in range(top[0], bottom[1] + 1):
                if len(result) < total:
                    result.append(matrix[top[0]][j])
        
            # top to bottom
            for j in range(top[0] + 1, bottom[0] + 1):
                if len(result) < total:
                    result.append(matrix[j][bottom[1]])

            # right to left
            for j in range(bottom[1] - 1, top[1], -1):
                if len(result) < total:
                    result.append(matrix[bottom[0]][j])

            # bottom to top
            for j in range(bottom[0], top[0], -1):
                if len(result) < total:
                    result.append(matrix[j][top[1]])

            top[0] += 1
            top[1] += 1
            bottom[0] -= 1
            bottom[1] -= 1

        return result

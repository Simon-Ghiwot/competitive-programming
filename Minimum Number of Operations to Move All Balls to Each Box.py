class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0] * len(boxes)
        for i in range(len(boxes)):
            total = 0
            for j in range(i + 1, len(boxes)):
                if boxes[j] == "1":
                    total += j - i
            for j in range(i - 1, -1, -1):
                if boxes[j] == "1":
                    total += i - j
            result[i] = total
        return result

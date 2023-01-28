class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = deque()
        maximum.append(arr[len(arr) - 1])
        for i in range(len(arr) - 2, -1, -1):
            if maximum[-1] < arr[i]:
                maximum.append(arr[i])
            else:
                maximum.append(maximum[-1])

        maximum.pop()
        for i in range(len(arr) - 1):
            arr[i] = maximum.pop()
        arr[len(arr) - 1] = -1
        return arr

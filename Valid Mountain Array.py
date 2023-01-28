class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        # increasing
        decreasing = increasing = False
        i = 0
        while i < len(arr) - 1:
            if arr[i] == arr[i + 1] or i == 0 and arr[i] > arr[i + 1]:
                return False
            elif arr[i] > arr[i + 1] :
                increasing = True
                break
            i += 1

        while i < len(arr) - 1:
            if arr[i] > arr[i + 1]:
                decreasing = True
            elif arr[i] <= arr[i + 1]:
                return False
            i += 1

        return increasing and decreasing 

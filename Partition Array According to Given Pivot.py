class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser, equal, greater = [], [], []
        for i in range(len(nums)):
            if nums[i] == pivot:
                equal.append(nums[i])
            elif nums[i] > pivot:
                greater.append(nums[i])
            else:
                lesser.append(nums[i])
        return [*lesser, *equal, *greater]

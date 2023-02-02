class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []

        def find_max(last):
            max_index = 0
            for i in range(last):
                if arr[max_index] < arr[i]:
                    max_index = i
            return max_index

        for i in range(len(arr)):
            maximum = find_max(len(arr) - i)
            if arr[maximum] != maximum + 1:

                # placing the largest element at the first postion
                temp = arr[:maximum + 1][::-1]
                temp.extend(arr[maximum + 1 :])
                
                # placing the largest value at the correct position
                temp2 = temp[: len(arr) - i][::-1]
                temp2.extend(temp[len(arr) - i :])
                arr = temp2
                
                # appending the indices
                result.append(maximum + 1)
                result.append(len(arr) - i)

        return result

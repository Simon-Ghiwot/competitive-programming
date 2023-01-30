class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(first, second):
            if int(first + second) < int(second + first):
                return 1
            return -1
        
        string_nums = [str(num) for num in nums]
        sorted_nums = sorted(string_nums, key = cmp_to_key(comparator))

        result = int("".join(sorted_nums))

        return str(result)

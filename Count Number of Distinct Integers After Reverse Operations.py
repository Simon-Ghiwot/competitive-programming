class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        unique = set()
        
        for num in nums:
            unique.add(num)
            string_num = str(num)
            reverse = int(string_num[::-1])
            unique.add(reverse)

        return len(unique)
        # 3 minutes

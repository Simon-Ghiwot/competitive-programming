class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        combined = []
        for i in range(len(plantTime)):
            combined.append([growTime[i], plantTime[i]]);

        combined.sort(reverse = True)
        max_bloom = day = -1
        for plant in combined:
            day += plant[1]
            max_bloom = max(max_bloom, day + 1 + plant[0])

        return max_bloom

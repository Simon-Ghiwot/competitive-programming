class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        partition = len(skill) // 2
        expected = total // partition
        if total % partition != 0:
            return -1
        skill.sort()
        left, right = 0, len(skill) - 1
        result = 0
        while left < right:
            if skill[left] + skill[right] != expected:
                return -1
            result += skill[left] * skill[right]
            left += 1
            right -= 1
        return result
        

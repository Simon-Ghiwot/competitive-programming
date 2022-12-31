class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary) - 2
        return (sum(salary) - salary[0] - salary[n + 1]) / n

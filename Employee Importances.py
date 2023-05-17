"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        idx = -1
        for i in range(len(employees)):
            if employees[i].id == id:
                idx = i
                break
        total = employees[idx].importance
        for subordinate in employees[idx].subordinates:
            total += self.getImportance(employees, subordinate)
        return total

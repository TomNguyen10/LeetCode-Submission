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
        imp = {}
        sub = {}
        for employee in employees:
            imp[employee.id] = employee.importance
            sub[employee.id] = employee.subordinates
        q = deque([id])
        res = 0
        while q:
            current = q.popleft()
            res += imp[current]
            for s in sub[current]:
                q.append(s)
        return res

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        big = max(milestones)
        total = sum(milestones) 
        if total - big < big:
            return 2 * (total - big) + 1
        return total


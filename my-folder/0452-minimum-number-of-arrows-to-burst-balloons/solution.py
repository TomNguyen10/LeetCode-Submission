class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0

        points = sorted(points, key = lambda x: x[1])

        res = 1

        end = points[0][1]

        for start, ePoint in points[1:]:
            if start > end:
                res += 1
                end = ePoint
        
        return res

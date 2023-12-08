class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(points)):
            cur_x, cur_y = points[i]
            prev_x, prev_y = points[i-1]
            res += max(abs(cur_x - prev_x), abs(cur_y - prev_y))
        return res

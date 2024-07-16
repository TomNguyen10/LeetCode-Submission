class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1-x2 == 0:
                return inf
            return (y1-y2)/(x1-x2)
        
        res = 1

        for i in range(len(points)):
            slopes = defaultdict(int)
            for j in range(i+1, len(points)):
                slope = find_slope(points[i], points[j])
                slopes[slope] += 1
                res = max(res, slopes[slope])
        
        return res + 1

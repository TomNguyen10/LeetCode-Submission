class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0

        sorted_arr = sorted(points, key = lambda x: x[1])

        count = 1

        end_point = sorted_arr[0][1]

        for start, end in sorted_arr[1:]:
            if start > end_point:
                end_point = end
                count += 1
        
        return count

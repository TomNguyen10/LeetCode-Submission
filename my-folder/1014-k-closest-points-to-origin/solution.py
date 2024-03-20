import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(heap, (distance, point))
        
        closest_points = []
        for _ in range(k):
            closest_points.append(heapq.heappop(heap)[1])
        
        return closest_points


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        max_heap = [-a, -b, -c]  
        heapq.heapify(max_heap)  
        res = 0
        while len(max_heap) > 1:
            num1 = -heapq.heappop(max_heap)  
            num2 = -heapq.heappop(max_heap)  
            if num1 - 1 > 0:
                heapq.heappush(max_heap, - (num1 - 1))
            if num2 - 1 > 0:
                heapq.heappush(max_heap, - (num2 - 1)) 
            res += 1
        return res

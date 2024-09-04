class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 1
        right = 10**7 + 1

        while left < right:
            middle = (left + right) // 2
            curr = 0
            for i in range(len(dist) - 1):
                curr += ceil(dist[i]/middle)
            curr += dist[-1]/middle
            if curr > hour:
                left = middle + 1
            else:
                right = middle
        
        if left == 10**7 + 1:
            return -1
        return left


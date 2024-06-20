class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        left = 0
        right = max(bloomDay)

        res = -1

        while left <= right:
            mid = (left + right) // 2

            num = 0

            count = 0

            for day in bloomDay:
                if day <= mid:
                    count += 1
                else:
                    count = 0
                
                if count == k:
                    num += 1
                    count = 0
            
            if num >= m:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res

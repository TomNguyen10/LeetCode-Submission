class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # left = 1
        # right = max(piles)
        # while left < right:
        #     mid = (right + left) // 2
        #     hours = 0
        #     for pile in piles:
        #         hours += ceil(pile / mid)
        #     if hours <= h:
        #         right = mid
        #     else:
        #         left = mid + 1
        # return right

        left = 1
        right = max(piles)
        while left < right:
            middle = (left+right)//2
            hour = 0
            for i in piles:
                hour += ceil(i/middle)
            if hour <= h:
                right = middle
            else:
                left = middle+1     
        return right

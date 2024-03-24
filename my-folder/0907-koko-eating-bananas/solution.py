class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            middle = (right + left) // 2
            hours = 0
            for pile in piles:
                hours += ceil(pile / middle)
            if hours <= h:
                right = middle
            else:
                left = middle + 1
        return right

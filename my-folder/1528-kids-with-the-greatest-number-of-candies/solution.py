class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolean = [False] * len(candies)
        max_candies = max(candies)
        for i in range(len(candies)):
            if extraCandies + candies[i] >= max_candies:
                boolean[i] = True
        return boolean
        

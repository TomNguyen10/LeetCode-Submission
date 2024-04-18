class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        al = []
        for restaurant in restaurants:
            if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
                if (veganFriendly == 0 or restaurant[2] == 1):
                    al.append(restaurant)
        sorted_list = sorted(al, key=lambda x: (-x[1], -x[0]))
        res = [li[0] for li in sorted_list]
        return res

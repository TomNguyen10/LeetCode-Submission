class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        map = {}
        items = items1 + items2
        for value, weight in items:
            if value not in map:
                map[value] = 0
            map[value] += weight
        
        res = [[value, weight] for value, weight in sorted(map.items())]

        return res
        


        

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        max_heap = []
        for i in range(len(score)):
            heappush(max_heap, (-score[i], i))

        res = [''] * len(score) 
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank = 0  
        while max_heap:
            s, index = heappop(max_heap)
            rank += 1 
            if rank <= 3:
                res[index] = medals[rank - 1]
            else:
                res[index] = str(rank)

        return res


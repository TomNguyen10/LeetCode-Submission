class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counts = [0] * (n+1)

        for i in citations:
            if i > n:
                counts[n] += 1
            else:
                counts[i] += 1
        
        papers = 0

        for i in range(n, -1, -1):
            papers += counts[i]
            if papers >= i:
                return i
        
        return 0

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0] * (n+1)
        for num in citations:
            if num >= n:
                bucket[n] += 1
            else:
                bucket[num] += 1
        count = 0
        for i in reversed(range(len(bucket))):
            count += bucket[i]
            if count >= i:
                return i
        return -1
        

class Solution:
    def movesToMakeZigzag(self, A: List[int]) -> int:
        A = [float('inf')] + A + [float('inf')]
        res = [0, 0]
        for i in range(1, len(A) - 1):
            res[i % 2] += max(0, A[i] - min(A[i - 1], A[i + 1]) + 1)
        return min(res) 

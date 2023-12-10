class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = zip(*matrix)
        return res

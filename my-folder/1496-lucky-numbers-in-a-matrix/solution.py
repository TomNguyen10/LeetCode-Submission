class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])

        res1 = float('-inf')

        for i in range(rows):
            min_val = min(matrix[i])
            res1 = max(min_val, res1)
        
        res2 = float('inf')

        for i in range(cols):
            max_val = max(matrix[j][i] for j in range(rows))
            res2 = min(res2, max_val)
        
        if res1 == res2: return [res1]

        return []

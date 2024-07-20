class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)

        currRow = [0] * rows
        currCol = [0] * cols

        res = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                res[i][j] = min(rowSum[i] - currRow[i], colSum[j] - currCol[j])
                currRow[i] += res[i][j]
                currCol[j] += res[i][j]
        
        return res

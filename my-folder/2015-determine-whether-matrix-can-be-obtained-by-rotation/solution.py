class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        c90, c180, c270, c360 =0, 0, 0, 0
        for i in range(n):
            for j in range(n):
                if(target[i][j]==mat[n-j-1][i]):
                    c90 += 1
                if(target[i][j]==mat[n-i-1][n-j-1]):
                    c180 += 1
                if(target[i][j]==mat[j][n-i-1]):
                    c270 += 1
                if(target[i][j]==mat[i][j]):
                    c360 += 1
        
        if c90 == n*n or c180 == n*n or c270 == n*n or c360 == n*n:
            return True
        return False

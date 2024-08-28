class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        '''
        1. We will first create a matrix dp to store the path since one path can be explored multiple times, the Matrix index dp[i][j] will store if there exists a path from this index or not.

        2. If we are at i’th index of s1 and j’th index of s2 and s3[i+j] matches both s1[i] and s2[j] then we explore both the paths that are we will go right and down i.e. we will explore index i+1,j and j+1,i.

        3. If s3[i+j] only matches with s1[i] or s2[j] then we will go just down or right respectively that is i+1,j or i,j+1.
        '''
        m = len(s1)
        n = len(s2)

        dp = [[False] * (n+1) for _ in range(m+1)]

        if m + n != len(s3):
            return False

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                
                elif i == 0:
                    if s2[j-1] == s3[j-1]:
                        dp[i][j] = dp[i][j-1]
                
                elif j == 0:
                    if s1[i-1] == s3[i-1]:
                        dp[i][j] = dp[i-1][j]
                
                elif s1[i-1] == s3[i + j - 1] and s2[j-1] != s3[i + j - 1]:
                    dp[i][j] = dp[i-1][j]
                
                elif s1[i-1] != s3[i + j - 1] and s2[j-1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j-1]
                
                elif s1[i-1] == s3[i+j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                
            
        return dp[m][n]

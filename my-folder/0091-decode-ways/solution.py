class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        Bottom up approach:
        Used a 1-d array to keep track of each substring
        dp[0] means empty string and 0 ways to decode
        Check every one and two digit combination along the way
        '''

        n = len(s)

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, n+1):
            first = int(s[i-1:i])
            second = int(s[i-2:i])
            if 1 <= first <= 9:
                dp[i] += dp[i-1]
            if 10 <= second <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]


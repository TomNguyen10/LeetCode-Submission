class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for word in wordDict:
                length = len(word)
                if length <= i and dp[i - length] and s[i-length:i] == word:
                    dp[i] = True
                    break
        
        return dp[n]

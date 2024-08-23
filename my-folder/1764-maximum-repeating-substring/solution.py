class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        s = len(sequence)
        w = len(word)

        dp = [0] * (s+1)

        res = 0

        for i in range(w, s+1):
            if (sequence[i-w:i] == word):
                dp[i] = dp[i-w] + 1
                res = max(res, dp[i])
        
        return res

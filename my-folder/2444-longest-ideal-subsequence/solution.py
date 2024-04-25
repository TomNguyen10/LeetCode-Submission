class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        res = 1
        for c in s:
            i = ord(c) - ord('a')
            dp[i] += 1
            for j in range(max(0, i - k), min(25, i + k)+1):
                if i != j:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res


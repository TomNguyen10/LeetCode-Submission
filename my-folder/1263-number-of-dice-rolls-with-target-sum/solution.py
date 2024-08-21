class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        mod = 10**9 + 7
        def dp(dice, target):
            if target > k * dice:
                memo[dice, target] = 0
                return 0
            if dice == 0: return target == 0
            if target < 0: return 0

            if (dice, target) in memo: return memo[dice, target]

            res = 0

            for i in range(1, k + 1):
                res += dp(dice-1, target - i)
            
            memo[dice, target] = res

            return res
        
        return dp(n, target) % mod

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        count = 0
        def reverse(num):
            return int(str(num)[::-1])
        diff_count = {}
        for num in nums:
            diff = num - reverse(num)
            count += diff_count.get(diff, 0)
            diff_count[diff] = diff_count.get(diff, 0) + 1
        return count % MOD

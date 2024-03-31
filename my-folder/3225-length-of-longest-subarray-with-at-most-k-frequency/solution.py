class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        dic = defaultdict(int)
        left = 0
        right = 0
        while right < len(nums):
            dic[nums[right]] += 1
            while dic[nums[right]] > k:
                dic[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res

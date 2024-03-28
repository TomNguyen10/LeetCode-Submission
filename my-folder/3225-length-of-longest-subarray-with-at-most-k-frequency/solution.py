class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        res = 0
        count = defaultdict(int)
        left = right = 0

        while right < len(nums):
            count[nums[right]] += 1

            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        
        return res

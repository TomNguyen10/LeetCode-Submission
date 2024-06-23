class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        left = right = 0
        count = 0
        while right < len(nums):
            if nums[right] % 2 == 1:
                k-= 1
                count = 0
            while k == 0:
                if nums[left] % 2 == 1:
                    k += 1
                left += 1
                count += 1
            res += count
            right += 1
        return res

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(arr, num):
            left = 0
            res = 0
            count = defaultdict(int)
            for right in range(len(nums)):
                if count[arr[right]] == 0: num -= 1
                count[arr[right]] += 1
                while num < 0:
                    count[arr[left]] -= 1
                    if count[arr[left]] == 0: num += 1
                    left += 1
                res += right - left + 1
            return res
        
        ans = atMostK(nums, k) - atMostK(nums, k - 1)

        return ans

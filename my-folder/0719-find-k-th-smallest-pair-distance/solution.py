class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def countPairs(nums, distance):
            res = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > distance:
                    left += 1
                res += right - left
            return res    
        
        nums.sort()
        min_val = nums[0]
        max_val = nums[-1]

        low = 0
        high = max_val - min_val

        while low < high:
            mid = (low + high) // 2

            count = countPairs(nums, mid)

            if count < k:
                low = mid + 1
            else:
                high = mid
            
        return low


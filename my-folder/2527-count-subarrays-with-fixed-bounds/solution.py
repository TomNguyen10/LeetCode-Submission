class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bound = -1 
        minIdx = -1 
        maxIdx = -1
        res = 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK: bound = i
            if nums[i] == maxK: maxIdx = i
            if nums[i] == minK: minIdx = i
            res += max(0, min(maxIdx, minIdx) - bound)

        return res

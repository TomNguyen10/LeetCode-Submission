class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        arr = [0] * 1001

        for num in nums:
            for i in num:
                arr[i] += 1
        
        res = []

        for i in range(1, len(arr)):
            if arr[i] == len(nums):
                res.append(i)
        
        return res

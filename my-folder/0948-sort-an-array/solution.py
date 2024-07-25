class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        max_val = max(nums)
        min_val = min(nums)
        
        if min_val < 0:
            bucket_neg = [0] * (-min_val + 1)
        else:
            bucket_neg = []

        if max_val >= 0:
            bucket_pos = [0] * (max_val + 1)
        else:
            bucket_pos = []

        for num in nums:
            if num >= 0:
                bucket_pos[num] += 1
            else:
                bucket_neg[-num] += 1
        
        res = []

        for i in range(len(bucket_neg) - 1, -1, -1):
            res.extend([-i] * bucket_neg[i])
        
        for i in range(len(bucket_pos)):
            res.extend([i] * bucket_pos[i])
        
        return res

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = {0: 1}
        cum = 0
        res = 0

        for num in nums:
            cum += num
            if cum - goal in dic:
                res += dic[cum-goal]
            dic[cum] = dic.get(cum, 0) + 1
        
        return res

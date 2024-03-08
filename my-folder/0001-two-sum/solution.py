class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        res = [-1] * 2
        for i in range(len(nums)):
            val = target - nums[i]

            if val in dic:
                res[0] = dic[val]
                res[1] = i
            
            else:
                dic[nums[i]] = i
        
        return res

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = 0
        dic = {0: -1}

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in dic:
                if i - dic[prefix_mod] > 1:
                    return True
            
            else:
                dic[prefix_mod] = i
        
        return False

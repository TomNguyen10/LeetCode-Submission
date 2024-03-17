class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0: 0}
        res = 0
        count = 0

        for index, num in enumerate(nums, 1):
            if num == 0: count -= 1
            else: count += 1
            
            if count in dic:
                res = max(res, index - dic[count])
            else:
                dic[count] = index
            
        return res


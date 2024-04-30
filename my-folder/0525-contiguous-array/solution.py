class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0: -1}
        current_sum = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_sum += 1
            else:
                current_sum -= 1
            if current_sum in dic:
                res = max(res, i - dic[current_sum])
            else:
                dic[current_sum] = i
        return res

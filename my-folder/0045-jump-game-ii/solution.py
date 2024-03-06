class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curEnd = 0
        curFar = 0

        for i in range(len(nums)-1):
            curFar = max(curFar, i + nums[i])

            if i == curEnd:
                curEnd = curFar
                jumps += 1
        
        return jumps

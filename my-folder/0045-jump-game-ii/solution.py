class Solution:
    def jump(self, nums: List[int]) -> int:
        # The main idea is based on greedy. 
        # Let's say the range of the current jump is [curBegin, curEnd], curFarthest is the farthest point that all points in [curBegin, curEnd] can reach. 
        # Once the current point reaches curEnd, then trigger another jump, and set the new curEnd with curFarthest, then keep the above steps, as the following:

        res = 0
        curEnd = 0
        curFar = 0

        for i in range(len(nums) - 1):
            curFar = max(curFar, i + nums[i])
            if i == curEnd:
                res += 1
                curEnd = curFar

        return res
        


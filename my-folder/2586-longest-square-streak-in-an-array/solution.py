class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in dic:
                dic[num] = i
        res = -1
        for i in range(len(nums)):
            x = nums[i]
            lt = [x]
            while True:
                if x**2 in dic:
                    x = x**2
                    lt.append(x)
                    print(lt)
                    res = max(len(lt), res)
                else:
                    break
        return res

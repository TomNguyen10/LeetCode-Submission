class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        res = [0] * n
        for i in range(n-1, -1, -1):
            l = nums[left]**2
            r = nums[right]**2
            if l >= r:
                res[i] = l
                left += 1
            else:
                res[i] = r
                right -= 1
        return res

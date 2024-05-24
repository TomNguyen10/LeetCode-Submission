class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def backtrack(nums, index, temp):
            self.res.append(temp[:])
            for i in range(index, len(nums)):
                temp.append(nums[i])
                backtrack(nums, i + 1, temp)
                temp.pop()
        backtrack(nums, 0, [])
        return self.res

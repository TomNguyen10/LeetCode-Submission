class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        s = set(nums)
        dic = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(nums)):
            dic[nums[right]] += 1
            while len(dic) == len(s):
                dic[nums[left]] -= 1
                if dic[nums[left]] == 0:
                    del dic[nums[left]]
                left += 1
            res += left
        
        return res

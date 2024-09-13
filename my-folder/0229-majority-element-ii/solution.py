class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []
        for key, val in c.items():
            if val > len(nums) // 3:
                res.append(key)
        return res

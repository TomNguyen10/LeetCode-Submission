class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        c = c1 & c2
        res = []
        for key, val in c.items():
            res.extend([key] * val)
        return res

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        longer = nums1 if len(nums1) > len(nums2) else nums2
        shorter = nums2 if len(nums1) > len(nums2) else nums1

        ans = []
        for i in shorter:
            if i in longer:
                longer.remove(i)
                ans.append(i)
        return ans

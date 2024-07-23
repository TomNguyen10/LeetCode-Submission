class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = defaultdict(int), defaultdict(int)
        for num in nums1:
            s1[num**2] += 1 
        for num in nums2:
            s2[num**2] += 1 
        res = 0
        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                cal = nums1[i] * nums1[j]
                if cal in s2:
                    res += s2[cal]
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                cal = nums2[i] * nums2[j]
                if cal in s1:
                    res += s1[cal]
        
        return res

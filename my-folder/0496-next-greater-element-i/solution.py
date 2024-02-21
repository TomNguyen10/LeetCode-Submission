class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                dic[stack.pop()] = num
            stack.append(num)
        for i in range(len(nums1)):
            nums1[i] = dic.get(nums1[i], -1)
        return nums1

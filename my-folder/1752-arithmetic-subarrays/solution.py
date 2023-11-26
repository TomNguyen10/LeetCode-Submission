class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        n = len(l)
        def helper(arr, dis):
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] != dis:
                    return False
            return True
        for i in range(n):
            sub = nums[l[i]:r[i]+1]
            sub.sort()
            dis = sub[1] - sub[0]
            add = helper(sub, dis)
            res.append(add)
        return res

        

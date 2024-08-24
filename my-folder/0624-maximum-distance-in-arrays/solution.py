class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        if len(arrays) <= 1: return res

        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        for i in range(1, len(arrays)):
            arr = arrays[i]
            case1 = max_val - arr[0]
            case2 = arr[-1] - min_val
            res = max(res, case1, case2)
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])
                 
        return res

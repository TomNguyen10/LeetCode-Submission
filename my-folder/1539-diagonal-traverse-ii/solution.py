class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = {}
        for i in range(len(nums)):
            n = len(nums[i])
            for j in range(n):
                if i + j not in m:
                    m[i+j] = []
                    m[i+j].append(nums[i][j])
                else:
                    m[i+j].append(nums[i][j])
        res = []
        for key in m:
            res.extend(m[key][::-1])
        return res
        
                
        

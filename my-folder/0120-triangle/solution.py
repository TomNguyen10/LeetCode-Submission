class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            curr = triangle[i]
            prev = triangle[i-1]
            
            for j in range(len(curr)):
                if j == 0:
                    curr[j] += prev[0]
                elif j == len(curr) - 1:
                    curr[j] += prev[-1]
                else:
                    curr[j] += min(prev[j], prev[j-1])
            
        return min(triangle[-1])
                

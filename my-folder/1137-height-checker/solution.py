class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height_freq = {}
        for height in heights:
            height_freq[height] = height_freq.get(height, 0) + 1
        
        count = 0
        
        i = 0
        for height in range(101): 
            if height in height_freq:
                while height_freq[height] > 0:
                    if heights[i] != height:
                        count += 1
                    i += 1
                    height_freq[height] -= 1
        
        return count


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            covered = False  
            for arr in ranges:
                if i in range(arr[0], arr[1] + 1):
                    covered = True
                    break
            if not covered:
                return False    

        return True

        

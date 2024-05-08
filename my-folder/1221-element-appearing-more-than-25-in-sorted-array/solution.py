class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        r = n // 4

        for i in range(n - r):
            if arr[i] == arr[i+r]:
                return arr[i]
        
        return -1

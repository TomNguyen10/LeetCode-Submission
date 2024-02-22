class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr = [0] * (n+1)
        for pair in trust:
            a, b = pair
            arr[b] += 1
            arr[a] -= 1
        
        for i in range(1, len(arr)):
            if arr[i] == n - 1:
                return i
        
        return -1

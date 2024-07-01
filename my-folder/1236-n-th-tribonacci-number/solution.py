class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0] * 38
        arr[1] = 1
        arr[2] = 1
        for i in range(len(arr)-3):
            arr[i+3] = arr[i] + arr[i+1] + arr[i+2]
        
        return arr[n]

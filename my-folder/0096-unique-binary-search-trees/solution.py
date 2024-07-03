class Solution:
    def numTrees(self, n: int) -> int:
        arr = [0] * (n+1)
        arr[1] = arr[0] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                left = j - 1
                right = i - j
                arr[i] += arr[left] * arr[right]

        return arr[n] 

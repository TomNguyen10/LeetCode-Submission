class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        max_h = max(heights)
        arr = [0] * (max_h+1)
        for num in heights:
            arr[num] += 1
        expected = []
        for i in range(len(arr)):
            if arr[i] != 0:
                expected.extend([i] * arr[i])
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res

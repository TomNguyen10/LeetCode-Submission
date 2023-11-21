class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int (sqrt(c))
        while left <= right:
            curr = left**2 + right**2
            print(curr)
            if curr == c:
                return True
            elif curr < c:
                left += 1
            else:
                right -= 1
        return False


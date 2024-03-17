class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n*(n+1)//2
        root = int(sqrt(total))
        if root**2 == total:
            return root
        return -1

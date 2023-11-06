class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        square = int (sqrt(n))
        if square * square != n:
            return False
        count = 2
        for i in range(2, square+1):
            if n % i == 0:
                count += 1
        return count == 3
        

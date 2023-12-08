class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        total = weeks/2 * (2*28 + (weeks - 1) * 7)
        total += ((days) * (days + 1) // 2) + (weeks * days) 
        return int (total)

        

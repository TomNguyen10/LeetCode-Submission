class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sumOfn = mean * (n + len(rolls)) - sum(rolls)
        if 6 * n < sumOfn or sumOfn < n:
            return []

        avg_roll = sumOfn // n
        remaining = sumOfn % n
        missing_rolls = [avg_roll] * n

        for i in range(remaining):
            missing_rolls[i] += 1

        return missing_rolls

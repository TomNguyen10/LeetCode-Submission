class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sumOfN = mean * (m + n) - sum(rolls)

        if 6*n < sumOfN or sumOfN < n:
            return []

        avg = sumOfN // n
        remain = sumOfN % n
        res = [avg] * n

        for i in range(remain):
            res[i] += 1
        
        return res

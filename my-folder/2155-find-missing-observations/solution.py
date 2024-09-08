class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n)
        nSum = total - sum(rolls)

        if nSum > 6 * n or nSum < 1 * n:
            return []

        avg = nSum // n
        remain = nSum % n
        res = [avg] * n

        for i in range(remain):
            res[i] += 1
        
        return res

        

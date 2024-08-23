class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1])
        for i in range(1, numRows):
            prev = res[-1]
            new = [1]

            for j in range(1, i):
                add = prev[j-1] + prev[j]
                new.append(add)
            new.append(1)
            res.append(new)
        return res

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                res = max(res, int (num[i]))
        if res == -1:
            return ""
        res = str(res) * 3
        return res

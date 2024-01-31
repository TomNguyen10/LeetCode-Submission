class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        stack = []
        stack.append(0)
        for i in range(1, len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                day = stack.pop()
                res[day] = i - day
            stack.append(i)
        return res


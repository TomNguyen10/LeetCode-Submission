class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for op in operations:
            if op == '+':
                num1 = res[-1]
                num2 = res[-2]
                res.append(num1+num2)
            elif op == 'D':
                num = res[-1]
                res.append(num*2)
            elif op == 'C':
                res.pop()
            else:
                res.append(int(op))
        
        return sum(res)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def helper(left, right, current):
            if left == 0 and right == 0:
                self.res.append(current[:])
                return
            if left > 0:
                helper(left - 1, right, current + '(')
            if right > left:
                helper(left, right - 1, current + ')')
        helper(n, n, "")
        return self.res

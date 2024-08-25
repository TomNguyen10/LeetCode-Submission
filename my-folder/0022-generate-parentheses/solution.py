class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Keep track of the number of open and close parentheses
        # If both equal to n we add it the list
        # We only add the close parenthese after the opening ones
        # If the number of open parentheses is smaller than n, add a new one
        # If the number of close parentheses is smaller than the opening ones, add a new one
        self.res = []
        def helper(current, open, close):
            if open == 0 and close == 0:
                self.res.append(current[:])
                return
            if open > 0:
                helper(current + '(', open-1, close)
            if open < close:
                helper(current + ')', open, close - 1)
        helper("", n, n)
        return self.res

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == '+':
                num = stack.pop() + stack.pop()
                stack.append(num)
            elif char == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif char == '*':
                num = stack.pop() * stack.pop()
                stack.append(num)
            elif char == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int (b / a))
            else:
                stack.append(int(char))
        
        return stack.pop()

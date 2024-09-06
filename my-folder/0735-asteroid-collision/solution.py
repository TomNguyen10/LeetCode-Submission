class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            if num < 0:
                while stack and stack[-1] > 0 and stack[-1] < abs(num):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(num)
                elif stack[-1] + num == 0:
                    stack.pop()
            else:
                stack.append(num)

        return stack

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = 0
        right = 0
        space = 0
        for c in moves:
            if c == 'L':
                left += 1
            elif c == 'R':
                right += 1
            else:
                space += 1
        
        return max(left, right) + space - min(left, right)

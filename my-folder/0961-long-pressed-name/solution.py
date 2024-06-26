class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1, p2 = 0, 0
        while p1 < len(name) and p2 < len(typed):
            if name[p1] == typed[p2]:
                p1 += 1
                p2 += 1
            elif p1 > 0 and name[p1 - 1] == typed[p2]:
                p2 += 1
            else:
                return False
        
        while p1 < len(name) and name[p1] == typed[p2 - 1]:
            p1 += 1
        
        while p2 < len(typed) and typed[p2] == typed[p2 - 1]:
            p2 += 1
        
        return p1 == len(name) and p2 == len(typed)


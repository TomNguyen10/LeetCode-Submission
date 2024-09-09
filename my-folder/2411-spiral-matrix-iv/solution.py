# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curDir = 0
        res = [[-1 for _ in range(n)] for _ in range(m)]

        if not head:
            return res
        
        x = 0
        y = 0

        while head:
            res[x][y] = head.val
            newX = x + directions[curDir][0]
            newY = y + directions[curDir][1]

            if newX < 0 or newY < 0 or newX >= m or newY >= n or res[newX][newY] != -1:
                curDir = (curDir + 1) % 4
            x += directions[curDir][0]
            y += directions[curDir][1]

            head = head.next
        
        return res

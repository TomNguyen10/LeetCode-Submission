# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]

        min_val = float('inf')

        prev = head
        curr = head.next
        pos = 1
        first = 0
        temp = 0

        while curr.next:
            if (curr.val < prev.val and curr.val < curr.next.val) or (curr.val > prev.val and curr.val > curr.next.val):
                if temp == 0:
                    temp = pos
                    first = pos
                else:
                    min_val = min(min_val, pos - temp)
                    temp = pos

            pos += 1
            prev = curr
            curr = curr.next
        
        if min_val != float('inf'):
            max_val = temp - first
            return [min_val, max_val]
        
        return res

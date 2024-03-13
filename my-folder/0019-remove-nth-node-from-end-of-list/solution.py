# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        start = end = dummy
        
        for _ in range(n):
            end = end.next
        
        while end.next:
            end = end.next
            start = start.next

        start.next = start.next.next

        return dummy.next

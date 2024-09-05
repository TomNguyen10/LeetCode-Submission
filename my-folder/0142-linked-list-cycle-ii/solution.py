# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
            
        fast = head
        slow = head

        while True:
            if not fast.next or not fast.next.next:
                return 
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        
        fast = head
        while fast != slow:
            fast= fast.next
            slow = slow.next
        
        return slow

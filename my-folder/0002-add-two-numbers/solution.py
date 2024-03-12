# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = start = ListNode(0)

        carry = 0

        while l1 or l2:
            s = carry

            if l1:
                s += l1.val
                l1 = l1.next
            
            if l2:
                s += l2.val
                l2 = l2.next
            
            node = ListNode(s%10)
            carry = s // 10
            dummy.next = node
            dummy = node
        
        if carry != 0:
            dummy.next = ListNode(carry)

        return start.next

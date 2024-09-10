# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        if not head.next:
            return head

        prev = head
        curr = head.next

        while curr:
            value = gcd(prev.val, curr.val)
            node = ListNode(value)

            prev.next = node
            node.next = curr

            prev = curr
            curr = curr.next
        
        return head

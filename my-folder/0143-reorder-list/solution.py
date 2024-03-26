# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        slow.next = None

        while curr:
            adj = curr.next
            curr.next = prev
            prev = curr
            curr = adj
        
        while prev:
            one = head.next
            two = prev.next
            head.next = prev
            prev.next = one
            head = one
            prev = two
        

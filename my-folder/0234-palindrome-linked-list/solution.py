# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, adj = None, None

        while slow:
            adj = slow.next
            slow.next = prev
            prev = slow
            slow = adj
        
        while head and prev:
            if head.val != prev.val: return False
            head = head.next
            prev = prev.next
        
        return True



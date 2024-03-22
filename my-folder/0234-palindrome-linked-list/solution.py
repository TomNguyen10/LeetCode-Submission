# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None
        adj = None

        while slow:
            adj = slow.next
            slow.next = prev
            prev = slow
            slow = adj
            
        first, second = head, prev

        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True

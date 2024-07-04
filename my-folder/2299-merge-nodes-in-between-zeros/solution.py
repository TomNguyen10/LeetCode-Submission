# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        sum = 0
        head = head.next

        while head:
            if head.val == 0:
                curr.next = ListNode(sum)
                curr = curr.next
                sum = 0
            else:
                sum += head.val
            head = head.next
        
        return dummy.next

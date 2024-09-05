# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        Keep track the list of element smaller and bigger than x by using pointers
        '''
        small = ListNode(0)
        big = ListNode(0)

        left = small
        right = big

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        
        left.next = big.next
        right.next = None

        return small.next

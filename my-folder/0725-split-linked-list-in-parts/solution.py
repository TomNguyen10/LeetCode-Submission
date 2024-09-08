# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [None] * k
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        split_size = size // k
        remain = size % k

        curr = head
        prev = curr

        for i in range(k):
            new_part = curr
            curr_size = split_size
            if remain > 0:
                remain -= 1
                curr_size += 1
            j = 0
            while j < curr_size:
                prev = curr
                if curr:
                    curr = curr.next
                j += 1
            
            if prev:
                prev.next = None
            
            res[i] = new_part
        
        return res

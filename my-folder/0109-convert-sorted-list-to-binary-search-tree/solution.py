# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        def convert(start, end):
            fast = slow = start
            if start == end:
                return None
            while fast!= end and fast.next != end:
                slow = slow.next
                fast = fast.next.next
            root = TreeNode(slow.val)
            root.left = convert(start, slow)
            root.right = convert(slow.next, end)
            return root
        
        return convert(head, None)

        

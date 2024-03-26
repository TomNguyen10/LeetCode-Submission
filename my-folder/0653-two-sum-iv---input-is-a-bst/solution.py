# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash_set = set()
        
        def traverse(root, s):
            if not root: return
            
            s.add(root.val)
            traverse(root.left, s)
            traverse(root.right, s)
        
        traverse(root, hash_set)
        print(hash_set)
        
        for num in hash_set:
            if k - num in hash_set and k - num != num: return True
        
        return False

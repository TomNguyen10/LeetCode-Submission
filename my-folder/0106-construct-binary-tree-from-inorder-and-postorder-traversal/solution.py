# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        map_order = {}

        for i in range(len(inorder)):
            val = inorder[i]
            map_order[val] = i

        def recur(low, high):
            if low > high:
                return None
            
            x = TreeNode(postorder.pop())
            mid = map_order[x.val]
            x.right = recur(mid+1, high)
            x.left = recur(low, mid-1)
            return x
        
        return recur(0, len(inorder) - 1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.toDel = set(to_delete)
        self.res = []
        def process(node):
            if not node: return

            node.left = process(node.left)
            node.right = process(node.right)

            if node.val in self.toDel:
                if node.left: self.res.append(node.left)
                if node.right: self.res.append(node.right)
                return None

            return node
        root = process(root)
        if root:
            self.res.append(root)
        return self.res

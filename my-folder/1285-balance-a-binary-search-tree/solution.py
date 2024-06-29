class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.list = []
        
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            self.list.append(node)
            inOrder(node.right)

        def build(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = self.list[mid]
            res = TreeNode(node.val)
            res.left = build(start, mid-1)
            res.right = build(mid+1, end)
            return res
        
        inOrder(root)
        return build(0, len(self.list) - 1)

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (subRoot == null || theSame(root, subRoot)) return true;
        if (root == null) return false;

        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    private boolean theSame(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;

        boolean left = theSame(p.left, q.left);
        boolean right = theSame(p.right, q.right);

        return left && right;
    }
}
